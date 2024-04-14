notaA = float(input("Informe a primeira nota: "))
notaB = float(input('Informe a segunda nota: '))

# calcular media
mediafinal = (notaA + notaB) / 2

# verificação
if mediafinal >= 7.0:
    print('Média: %.1f - Situação: Aprovado' % mediafinal)
else:
    print('Media: %.1f - Situação: Reprovado'% mediafinal)