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


