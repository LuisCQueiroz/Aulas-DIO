# Python
# Aula 04- Python

# Comentários

a = 1 # Variável de exemplo para comentários

# docstring

"""
    Este é um comentário
    que ocupa várias linha
"""

'''
    Que também pode ser
    com aspas simples
'''

print()
print("Se você pretende mesclar 'símbolos' diferentes, então faça isso.")
print()

print()
print("Se você pretende mesclar 'símbolos' diferentes, então faça isso.")
print('Ou isso "para alternar" entre aspas simples e duplas')
print()

#print

print('Teste de saída')
print('Teste de saída \nem várias linhas')

print('Curso', 'de', 'Python')

print('Curso', 'de', 'Python', sep=' | ') # separar as partes usando um caracter

print('Curso', 'de', 'Python', end='.') # finaliza a string com um determinad caracter
print()
print('Curso \t de \t Python') #separado por tabulaador

arquivo = open('Aula 04 - saida.txt','a+') # a+ adiciona uma linha nova no arquivo txt 
print('Curso', 'de', 'Python', file=arquivo)
print('Luis teste', file=arquivo)
arquivo.close()

print()

# Ctrl + S - Salva o script


