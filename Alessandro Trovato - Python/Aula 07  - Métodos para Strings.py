# Método é um procedimento que pode manipular atributos de objetos para qual
# o método foi chamado

print(type('texto'))
print('texto de exemplo'.capitalize())

# Concatenação de textos (strings)

textoA = "Curso"
textoB = "Python"
textoC = "Trovato"

resultado = textoA + " " +  textoB + " " + textoC

print(resultado)
print()
print(resultado.upper()) #Converte texto em maíusculas

print()

varA, varB = 99, 199
print(varA + varB)
print("Resultado " +str(varA + varB))
print()

# Métodos para os textos

varTexto = 'Curso Python Trovato'

# Preenchimento com caracteres

print(varTexto.ljust(50,'.')) # preenche a esquerda(L) com 50 caracteres ponto
print(varTexto.ljust(50) + '|') # preenche com 50 caracteres vazios e coloca | no final
print()
print(varTexto.rjust(50,'-')) # preenche a direita(R) com 50 caracteres traço
print(varTexto.rjust(50)) # preenche com 50 caracteres vazios ao lado direito
print()
print(varTexto.center(50,'-'))
print(varTexto.center(50))
print()

# Repetição de caracteres
print('x' * 15)
print()

# Alteração da caixa de palavras A/a
varTexto = 'curso Python trovato'
print('Resultado do método title()', varTexto.title())
print()
print('luis carlos'.title())
print()

print(varTexto.upper()) # converte todo o texto em maiuscula
print(varTexto.lower()) # converte todo o texto em minúscula
print()

print('Alessandro'.swapcase())
print()

#Função Len (tamanho de uma string
print(len(varTexto))
print()

#Extração de texto
print(varTexto[0]) # apresenta a primeira letra, podendo ser utilizado outo número
print(varTexto[0:5]) # apresenta os 5 caracteres a partir da posição 0
print(varTexto[6:])
print(varTexto[:5])

# Eliminar espaços
varTexto = '               Exemplo           '
print("Tamanho antes da limpeza: ",len(varTexto))
print(varTexto.strip())
print("Tamanho depois da limpeza: ",len(varTexto.strip()))
print()

# Concatnar caracteres a sua string
varTexto = "Curso de Python Trovato"
print('-'.join(varTexto))
print()










