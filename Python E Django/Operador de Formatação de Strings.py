# Operador de formatação de Strings

# d - Inteiro com sinal (também pode ser usadi i no lugar de d)
print('Hoje é dia %d' % 15)

# o - Valor na base Octal, converte números para Octal
print('12 em octal é %o' %12)

# x - Valor na base hexadecimal, converte números para hexadecimal
print('255 em hexadecimal é %x' % 255)

# .QtdeCasasDecimais - imprime um número decimal com a quantidade de casas informadas
# depois do ponto
# f - Número de ponto flutuante - decimal
print('Pi com duas casas decimais é aproximadamente %.2f' %3.1415926)
print('Pi com três casas decimais é aproximadamente %.3f' %3.1415926)

# s (string) Inprime um texto literal na posição
nome = 'Luis Carlos de Queiroz'
print('Meu nome é %s' % nome)
