# Declare 4 variáveis do tipo numérica
a = 5
b = 6
c = 8
d = 15

# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem 
# informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem 
# informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas 
# utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, 
# e use apenas a palavra reservada "if"
if (a <= b):
    print(f"A condição foi cumprida. O número {b} é maior que {a}")
else:
    print(f"A condição não foi cumprida. O número {a} é maior que {b} ")

if (d <= c):
    print(f"A condição foi cumprida. O número {c} é maior que {d}")
else:
    print(f"A condição não foi cumprida. O número {d} é maior que {c} ")

if (a <= b) and (c <= d):
    print("A condição foi cumprida. ")
else:
    print("A condição não foi cumprida.")
