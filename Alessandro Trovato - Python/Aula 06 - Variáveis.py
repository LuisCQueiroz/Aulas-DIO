# Tipos primitivos de dados em Python
# int          | Inteiro    
# float        | Reais ou Ponto Flutuante
# boolean      | Booleano (True ou False)
# complex      | Tipo Complexo
# string       | Alfanuméricos

# Variáveis de Texto
texto = "Curso de Python - Trovato"  # atribuição

print(texto)
print(type(texto))
print()


varNumero1 = '100'
print(varNumero1)
print(type(varNumero1))
print()

# Variáveis para tipo Numéricos
varA = 99
varB = 4.56789
varC = False
varD = 2+9j
varE = 'Pyhton'

print(varA, varB, varC, varD, varE)
print()

print(type(varA), type(varB), type(varC), type(varD), type(varE))
print()

# Conversão de tipos

varF = float(varA)
print(varF)
print('Float de varF: ', type(varF))
print(type(varF))
print()

varG = int(varB)
print(varG)
print('Int de varG:', type(varG))
print()

# Variáveis Booleanas
varH = False
varI = True
varJ = not(False)
varK = not(True)

print(varH, varI, varJ, varK)
print()


