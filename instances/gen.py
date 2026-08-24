import random

def generate_dna_sequences(size1, size2, filename):
    bases = ['A', 'C', 'G', 'T']
    s1 = ''.join(random.choice(bases) for _ in range(size1))
    s2 = ''.join(random.choice(bases) for _ in range(size2))
    
    with open(filename, 'w') as f:
        f.write(f"{s1}\n{s2}")
    print(f"Instância gerada com sucesso em {filename} (Tamanhos: {size1}, {size2})")

if __name__ == "__main__":
    # Parâmetros da Progressão Aritmética
    valor_inicial = 5
    valor_final = 5000
    razao = 5
    
    # range(início, limite_superior, passo) gera a PA automaticamente.
    # Usamos +1 no valor final porque o range não inclui o último número por padrão.
    tamanhos = range(valor_inicial, valor_final + 1, razao)
    
    # Percorre a PA, cria o nome do arquivo e gera as sequências
    for tamanho in tamanhos:
        nome_arquivo = f"dna_{tamanho}.txt"
        generate_dna_sequences(tamanho, tamanho, nome_arquivo)