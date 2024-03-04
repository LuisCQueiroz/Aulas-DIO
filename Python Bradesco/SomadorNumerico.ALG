Algoritmo "SomadorNumerico"
// Solicita 10 numeros e realiza a soma deles
Var
   // Seção de Declarações das variáveis
   contador, N, soma, maior : Inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   contador <- 1
   soma <- 0
   maior <- 0

   
   Enquanto (contador <= 10) faca
      Escreva("Digite o ", contador, "o. valor: ")
      Leia (N)
      Se (N > maior) entao
         maior <- N
      FimSe
      soma <- soma + N

      contador <- contador + 1
   FimEnquanto
   Escreval ("A soma dos valores foi: ", soma)
   Escreval ("O maior número digitado foi: ", maior)
Fimalgoritmo