ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade = ano_formatura - ano_nascimento
print(f"A idade de Gerlaine é {idade} anos")

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura > ano_nascimento)
print(ano_formatura >= ano_nascimento)
print(ano_formatura < ano_nascimento)
print(ano_formatura <= ano_nascimento)
print(ano_formatura == ano_nascimento)
print(ano_formatura != ano_nascimento)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print("Expressões comparativas com operadores lógicos")
print((ano_formatura > ano_nascimento) or (ano_formatura >= ano_nascimento))
print((ano_formatura < ano_nascimento) and (ano_formatura <= ano_nascimento))
print(not(ano_formatura != ano_nascimento))