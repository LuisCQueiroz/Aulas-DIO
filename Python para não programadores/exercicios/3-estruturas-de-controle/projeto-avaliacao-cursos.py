# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos =['Introdução a SQL', 'Python: Formação Básica', 'Python para Ciência de Dados: Formação Básica', 'Descubra a linguagem de programação R', 'Fundamentos de Programação: Algoritmos']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_git = 'Git e GitHub: Formação Básica'
curso_python = 'Python: Formação Básica'
curso_r = 'Descubra a linguagem de programação R'
# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliações = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print()
if curso_python in cursos:
    print(f"O curso {curso_python} está no catálogo. Por favor, avalie o curso")
    avaliações[curso_python] = int(input("Informe uma nota de 0 a 5: "))
else:
    print(f"Infelizmente o curso {curso_python} não compõe nosso catálogo")
print()

if curso_git in cursos:
    print(f"O curso {curso_git} está no catálogo. Por favor, avalie o curso")
    avaliações[curso_git] = int(input("Informe uma nota de 0 a 5: "))
else:
    print(f"Infelizmente o curso {curso_git} não compõe nosso catálogo")
print()

if curso_r in cursos:
    print(f"O curso {curso_r} está no catálogo. Por favor, avalie o curso")
    avaliações[curso_r] = int(input("Informe uma nota de 0 a 5: "))
else:
    print(f"Infelizmente o curso {curso_r} não compõe nosso catálogo")

print()
print(avaliações)