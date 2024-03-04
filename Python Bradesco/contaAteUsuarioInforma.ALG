Algoritmo "contaAteUsuarioInforma"

Var
   // Seção de Declarações das variáveis
   valor, salto, contador : Inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   contador <- 0
   Escreva("Quer contar ate quanto ? ")
   Leia(valor)
   Escreva("Qual sera o valor do salto? ")
   Leia(salto)
   Enquanto (contador <= valor ) faca
      EscrevaL(contador)

      contador <- contador + salto
   FimEnquanto
   EscrevaL("Terminei de contar")


Fimalgoritmo