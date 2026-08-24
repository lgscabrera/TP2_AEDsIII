#include "algoritmos.h"
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include <stdio.h>

/* Preencher os campos abaixo
Participantes do grupo
Nome: Joaquim Pedro do Nascimento Moreira de Jesus      Matrícula: 2025.1.08.014
Nome: Murilo Antonio da Silva                           Matrícula: 2025.1.08.0
Nome: Luiz Fernando Ferreira Cabral                     Matrícula: 2025.1.08.032
Nome: Victória Almeida Tambasco                         Matrícula: 2025.1.08.0
Nome: Luiz Gabriel da Silva Cabrera                     Matrícula: 2025.1.08.0
*/

bool comparacao_de_base_DNA(char b1, char b2) {
    if ((b1 == 'A' && b2 == 'T') || (b1 == 'T' && b2 == 'A') || (b1 == 'C' && b2 == 'G') || (b1 == 'G' && b2 == 'C'))
        return true;
    return false;
}

long int programacao_dinamica(char *s1, char *s2) {
    long int pontuacao = 0;
    
    int n = strlen(s1);
    int m = strlen(s2);

    // Cálculo da memória da matriz
    size_t memoria_matriz = (size_t)(n + 1) * (m + 1) * sizeof(int);

    int *matriz = malloc(memoria_matriz);

    if (matriz == NULL) {
        printf("Erro - Prog. Dinâmica\n");
        return INT_MIN; 
    }

    matriz[0] = 0;
    for(int j = 1; j <= m; j++) {
        matriz[j] = matriz[j - 1] - 2;
    }

    for(int i = 1; i <= n; i++) {
        int atual = i * (m + 1);
        int anterior = (i - 1) * (m + 1);
        matriz[atual] = matriz[anterior] - 2;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            int diag = i * (m + 1) + j; 
            int diag_ant = (i-1) * (m+1) + (j-1);
            int cima = (i-1) * (m + 1) + j;
            int esquerda = i * (m + 1) + (j-1);
            int score_diag;

            if (comparacao_de_base_DNA(s1[i-1], s2[j-1])) {
                score_diag = matriz[diag_ant] + 2;
            } else {
                score_diag = matriz[diag_ant] - 1;
            }

            int score_cima = matriz[cima] - 2; 
            int score_esq  = matriz[esquerda] - 2;

            int max = score_diag;
            if (score_cima > max) max = score_cima;
            if (score_esq > max) max = score_esq;

            matriz[diag] = max;  
        }
    }

    pontuacao = matriz[n * (m + 1) + m];
    
    // Exibição da memória utilizada
    // Somamos a matriz + variáveis administrativas locais aproximadas
    printf("Memória utilizada (Programação Dinâmica): %zu bytes\n", memoria_matriz + sizeof(int)*7);

    free(matriz);
    return pontuacao;
}

long int guloso(char *s1, char *s2) {
    long int pontuacao = 0;
    int i = 0, j = 0;
    int n = strlen(s1);
    int m = strlen(s2);

    while (i < n && j < m) {
        int score_diag = comparacao_de_base_DNA(s1[i], s2[j]) ? 2 : -1;
        int score_gap_s1 = -2; 
        int score_gap_s2 = -2; 

        if (score_diag >= score_gap_s1 && score_diag >= score_gap_s2) {
            pontuacao += score_diag;
            i++;
            j++;
        } 
        else if (score_gap_s1 >= score_gap_s2) {
            pontuacao += score_gap_s1;
            j++;
        } 
        else {
            pontuacao += score_gap_s2;
            i++;
        }
    }

    while (i < n) {
        pontuacao -= 2;
        i++;
    }
    while (j < m) {
        pontuacao -= 2;
        j++;
    }

    // O algoritmo guloso utiliza apenas variáveis locais na stack
    size_t memoria_total = sizeof(int) * 7 + sizeof(long int);
    printf("Memória utilizada (Guloso): %zu bytes\n", memoria_total);

    return pontuacao;
}