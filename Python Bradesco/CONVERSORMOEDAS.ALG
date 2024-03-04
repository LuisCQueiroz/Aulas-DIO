Algoritmo "conversorMoedas"                  /")

Var
   // Seção de Declarações das variáveis
   C, Q: Inteiro
   R, D: Real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   C <- 1
   Escreva("Quantas vezes você quer converter ? ")
   Leia(Q)
   
   Enquanto (C <= Q) faca
            Escreva("Qual o valor em R$? ")
            Leia (R)
            D <- R/2.20
            Escreval("O valor convertido é US$: ",D)
            C <- C + 1
   FimEnquanto
Fimalgoritmo