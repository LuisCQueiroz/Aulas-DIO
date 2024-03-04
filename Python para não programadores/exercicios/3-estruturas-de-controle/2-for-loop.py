# Crie uma lista
cursos_likedin_learning =['Introdução a SQL', 'Python: Formação Básica', 'Python para Ciência de Dados: Formação Básica', 'Descubra a linguagem de programação R', 'Fundamentos de Programação: Algoritmos']

# Crie um for loop para imprimir cada elemento dessa lista
for curso in cursos_likedin_learning:
    print(curso)

# Crie um objeto iterável utilizando a função range()
# range(inicio, fim, passo)
print()
print(list(range(5)))

print()
print(list(range(30, 40, 2)))

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
print()
for item in range(4, 7):
    print(f"{item} - Estou aprendendo uma linguagem de programação.")
else:
    print("Fim do loop.")
