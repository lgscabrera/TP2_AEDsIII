<div style="font-family: 'Courier New', Courier, monospace;">
  <h1 align="center">TP2 AED's III - Pareamento de sequência de DNA</h1>

  <section align="center">
    <h2>👥 Autores:</h2>
    <ul type="none">
      <li>Joaquim Pedro do Nascimento Moreira de Jesus</li>
      <li>Victória Almeida Tambasco</li>
      <li>Murilo Antonio da Silva</li>
      <li>Luiz Gabriel da Silva Cabrera</li>
      <li>Luiz Fernando Ferreira Cabral</li>
    </ul>
    <p><i>Trabalho desenvolvido em grupo conforme as diretrizes da disciplina.</i></p>
  </section>

  <hr>

  <section>
    <p>
      Este repositório contém o desenvolvimento do segundo trabalho prático da disciplina <b>AEDS 3 (DCE797)</b> do curso de Bacharelado em Ciência da Computação da Universidade Federal de Alfenas (UNIFAL).
    </p>
    <h2>🧬 Sobre o Projeto</h2>
    <p>
      O objetivo deste projeto é implementar e avaliar algoritmos para realizar o alinhamento (pareamento) de sequências de DNA. O problema consiste em encontrar a melhor forma de sobrepor duas sequências de nucleotídeos (A, T, C, G) para maximizar a pontuação de pareamento, respeitando as regras biológicas de formação da dupla hélice.
    </p>
    <h2>Regras de Pontuação</h2>
    <p>O alinhamento é pontuado da seguinte forma:</p>
    <ol>
      <li>
        <b>Base Pareada (Correta)</b>: +2 pontos (A com T, C com G).
      </li>
      <li>
        <b>Base Não Pareada</b>: -1 ponto.
      </li>
      <li>
        <b>Lacuna (Gap)</b>: -2 pontos (quando uma base é pareada com um espaço vazio "-").
      </li>
    </ol>
    <h2>🛠️ Algoritmos Implementados</h2>
    <p>O trabalho exige a resolução do problema utilizando dois paradigmas diferentes para análise de <i>trade-offs</i> entre eficiência e otimalidade:</p>
    <ul>
      <li><b>Programação Dinâmica</b>: Algoritmo que busca a solução ótima global do alinhamento.</li>
      <li><b>Algoritmo Guloso</b>: Implementação com foco em velocidade de execução, cuja otimalidade é testada em comparação à Programação Dinâmica.</li>
    </ul>
    <h2>📊 Relatório e Análise</h2>
    <p>Além do código, o projeto inclui uma análise experimental detalhada cobrindo:</p>
    <ul>
      <li><b>Metodologia</b>: Descrição da lógica de implementação de cada paradigma.</li>
      <li><b>Gráficos de Desempenho</b>: Relação entre o tamanho da entrada vs. Tempo de Execução e Consumo de Memória.</li>
      <li><b>Tabela de Resultados</b>: Comparação das pontuações obtidas por ambos os algoritmos em diversas instâncias de teste.</li>
    </ul>
    <h2>📁 Estrutura do Repositório</h2>
    <ul>
      <li><b>/src</b>: Código-fonte em C (arquivos <code>algoritmos.c</code> e <code>algoritmos.h</code>).</li>
      <li><b>/doc</b>: Relatório técnico em PDF e slides da apresentação.</li>
      <li><b>/instances</b>: Conjunto de instâncias de DNA utilizadas nos testes.</li>
    </ul>
    <p>
      <b>Professor:</b> Iago Augusto de Carvalho.<br>
      <b>Data de Entrega:</b> 12/04/2026 às 23h59.
    </p>
  </section>
  
  <section>
    <h2>🚀 Como Utilizar</h2>
    <h3>1. Compilação</h3>
    <p>Para compilar o código-fonte em C, você possui duas abordagens:</p>
    <ul>
      <li>
        <b>Compilação Manual (Necessária para o Testador):</b> Como o script automatizado de testes em Python busca por um executável com o nome <code>dna</code>, utilize o seguinte comando na pasta onde estão os arquivos <code>.c</code>:
        <br><br>
        <code>gcc base.c algoritmos.c -Wall -Wextra -g -o dna</code>
      </li>
      <br>
      <li>
        <b>Usando o Makefile:</b> O projeto conta com um Makefile configurado para avaliações padronizadas. Ao rodar simplesmente o comando <code>make</code>, ele utilizará as flags de aviso rigorosas gerando um executável padrão com o nome <code>base</code>.
      </li>
    </ul>
    <h3>2. Configuração Inicial</h3>
    <p>Antes de iniciar a bateria de testes automatizados, é essencial ajustar os caminhos no arquivo <code>testador.py</code> para refletirem o seu ambiente local.</p>
    <ul>
      <li>Abra o script <code>testador.py</code> e atualize as variáveis <code>instances_dir</code> (onde os casos de teste ficam) e <code>output_csv</code> (onde os resultados serão salvos).</li>
      <li><b>Importante:</b> A estrutura espera que o diretório de instâncias (<code>/instances/</code>) esteja na raiz do repositório (<code>/TP2-AEDs_III-Pareamento_DNA/</code>) e não dentro da pasta <code>/src/</code>.</li>
    </ul>
    <h3>3. Entendendo os Componentes e Fluxo de Execução</h3>
    <p>O ecossistema do projeto é dividido em três partes principais: geração de dados, processamento e automação da coleta de resultados.</p>
    <ul>
      <li>
        <b><code>algoritmos.c</code> e <code>algoritmos.h</code> (Lógica Central):</b><br>
        Aqui reside a implementação do alinhamento. A função de Programação Dinâmica aloca a matriz e calcula a solução global ótima para as sequências de DNA, baseada na regra de pontuação (Match: +2, Mismatch: -1, Gap: -2). A função do Algoritmo Guloso tenta encontrar a melhor sobreposição tomando a decisão ótima local para ser mais rápido. Ao final, o código em C imprime no terminal o score alcançado, o tempo de CPU e a quantidade de memória (bytes) consumida por cada paradigma.
      </li>
      <br>
      <li>
        <b><code>gen.py</code> (Gerador de Instâncias):</b><br>
        Este script cria a massa de dados (as cadeias de nucleotídeos aleatórias). Ele está pré-configurado para gerar pares de sequências de DNA que crescem em uma Progressão Aritmética. Ao rodá-lo, ele gera arquivos indo do tamanho 5 ao 5000 (saltando de 5 em 5) e os salva no formato <code>dna_X.txt</code>.
        <br><br>
        <code>python3 gen.py</code>
      </li>
      <br>
      <li>
        <b><code>testador.py</code> (Automação de Testes):</b><br>
        O orquestrador da análise experimental. Quando executado, ele lê todos os arquivos <code>.txt</code> gerados na pasta de instâncias e, em ordem crescente de tamanho, invoca o executável <code>./dna</code>. Utilizando Expressões Regulares (RegEx), ele captura o que o C imprime na tela (Resultado, Tempo e Memória para os dois algoritmos) e organiza essas informações de forma tabular. Ao final do processamento, ele exporta tudo automaticamente para um arquivo <code>results.csv</code> dentro da pasta <code>doc/</code>, deixando os dados prontos para a confecção dos gráficos de complexidade do relatório.
        <br><br>
        <code>python3 testador.py</code>
      </li>
    </ul>
  </section>
</div>