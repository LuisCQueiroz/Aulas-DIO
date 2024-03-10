# input - Obter dados
import math as m
print()
varNome = input("Digite seu nome: ")
print('Olá,', varNome + '!\n')

print('Calcular a área de uma circunferência.\n')
varRaio = input('Informe o raio da circunferência: ')
varResultado = m.pi * float(varRaio) ** 2
print('Area' , varResultado)
print('Comprimento', 2 * m.pi * float(varRaio))
print()

print('-' * 50)
print()

# 2 exemplo
#Converter Graus Celsius para Fahrenheit

varTemperatura = float(input('Digite o valor em Celsius: '))
varResultado = (varTemperatura * 1.8) + 32
print('Fahrenheit: ', varResultado)

print('-' * 50)
print()

#format
varTexto = '{0}, seja bem-vindo(a)!\n'
print(varTexto.format(varNome))

print('-' * 50)
print()

varIdade = 55
varProfissão = 'Faturista'
varTexto = '{0}, seja bem-vindo(a)! \nIdade: {1} \nProfissão: {2} \n'
print(varTexto.format(varNome,varIdade, varProfissão))

print('-' * 50)
print()

varResultado = m.pi * float(varRaio) ** 2
print('Area' , varResultado)
print('Comprimento: ', 2 * m.pi * float(varRaio))
print()

Res_Final = 'Área: {0:.1f}\n'
print(Res_Final.format(varResultado))


