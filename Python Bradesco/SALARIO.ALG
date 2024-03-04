Algoritmo "salario"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
   // Seção de Declarações das variáveis
   salario, descontoinss, descontoir, salariofim: Real



Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   salario <- 0
   descontoinss <- 0
   descontoir <- 0
   salariofim <- 0
   Escreva("Informe o valor do salario")
   Leia(salario)
   descontoinss <- (salario*0.085)
   descontoir <- (salario*0.05)
   salariofim  <- (salario - descontoinss - descontoir)
   Escreva("Ovalor do d")
   Escreva(salariofim)


Fimalgoritmo