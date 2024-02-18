notas = []

for c in range(3):
    codigo_aluno = input("Número Chamada: ")
    nome_aluno = input("Nome do Aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    media = (nota1+nota2+nota3+nota4)/4

    if media >= 5:
        situacao = "Aprovado"
    elif media == 4:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    
    resultado = [codigo_aluno,nome_aluno,nota1,nota2,nota3,nota4,media,situacao]

    notas.append(resultado)
print()

for n in notas:
    codigo_aluno = n[0]
    nome_aluno = n[1]
    nota1 = n[2]
    nota2 = n[3]
    nota3 = n[4]
    nota4 = n[5]
    media = n[6]
    situacao = n[7]

 
    print("O aluno",  nome_aluno, "tirou as notas:", nota1,
         ",", nota2,
         ",", nota3,
         ",", nota4,
          ", Média:", media,
          "- Sua situação é:",situacao
          )
print()