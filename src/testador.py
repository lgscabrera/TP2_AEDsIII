import os
import re
import subprocess

# 1. Configuração dos caminhos e executável
instances_dir = "/home/joaquim-pedro/TP2-AEDs_III-Pareamento_DNA/instances/"
output_csv = "/home/joaquim-pedro/TP2-AEDs_III-Pareamento_DNA/doc/results.csv"

# Assumindo que o executável 'dna' está na mesma pasta onde este script será rodado
executable = "./dna" 

# Função auxiliar para extrair o número do nome do arquivo para ordenação correta
def extract_number(filename):
    match = re.search(r'dna_(\d+)\.txt', filename)
    return int(match.group(1)) if match else 0

def main():
    # Garante que a pasta de destino (doc) exista
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Lista e ordena os arquivos
    arquivos = [f for f in os.listdir(instances_dir) if f.startswith("dna_") and f.endswith(".txt")]
    arquivos.sort(key=extract_number)

    # Abre o arquivo CSV para escrita
    with open(output_csv, "w", encoding="utf-8") as f_out:
        # Cabeçalho atualizado com colunas de memória
        f_out.write("Entrada;Resultado PD;Tempo PD;Memoria PD (bytes);Resultado Guloso;Tempo Guloso;Memoria Guloso (bytes);\n")

        print("Iniciando bateria de testes...\n")

        for arquivo in arquivos:
            filepath = os.path.join(instances_dir, arquivo)
            tamanho = extract_number(arquivo)
            
            print(f"Rodando teste para {arquivo}...")

            # Executa o programa C
            process = subprocess.run([executable, filepath], capture_output=True, text=True)
            saida = process.stdout

            # RegEx atualizadas para capturar Resultado, Tempo e agora Memória
            regex_dp = r"Programação Dinâmica:\s*Resultado:\s*(-?\d+)\s*Tempo:\s*([0-9.]+)"
            regex_mem_dp = r"Memória utilizada \(Programação Dinâmica\):\s*(\d+)"
            
            regex_guloso = r"Guloso:\s*Resultado:\s*(-?\d+)\s*Tempo:\s*([0-9.]+)"
            regex_mem_guloso = r"Memória utilizada \(Guloso\):\s*(\d+)"

            # Buscando os padrões na saída
            match_dp = re.search(regex_dp, saida)
            match_mem_dp = re.search(regex_mem_dp, saida)
            
            match_guloso = re.search(regex_guloso, saida)
            match_mem_guloso = re.search(regex_mem_guloso, saida)

            if match_dp and match_guloso and match_mem_dp and match_mem_guloso:
                # Extração de dados
                res_dp = match_dp.group(1)
                tempo_dp = match_dp.group(2).replace('.', ',')
                mem_dp = match_mem_dp.group(1)

                res_guloso = match_guloso.group(1)
                tempo_guloso = match_guloso.group(2).replace('.', ',')
                mem_guloso = match_mem_guloso.group(1)

                # Montagem da linha CSV
                linha_csv = f"{tamanho};{res_dp};{tempo_dp};{mem_dp};{res_guloso};{tempo_guloso};{mem_guloso};\n"
                f_out.write(linha_csv)
            else:
                print(f"[ERRO] Falha ao capturar todos os dados de {arquivo}.")
                # Útil para debug: caso a regex falhe, ele mostra o que o C printou
                if not match_mem_dp: print("Dica: Regex de memória DP não encontrou padrão.")

    print(f"\nConcluído! Todos os testes foram salvos em:\n{output_csv}")

if __name__ == "__main__":
    main()