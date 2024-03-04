# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou 
# durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), 
# solicite o total de dias dedicados ao estudo por semana;

# 3. Crie uma variável chamada "total_horas" e, usando o método input(), 
# solicite a média de horas estudada por dia;

# 4. Crie uma variável chamada "curso" e, usando o método input(),
# solicite o título do curso desejado;

# 5. Imprima na tela uma frase usando o string format informando o nome da estudante, 
# o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input("Digite seu nome: ")
total_dias = int(input("Digite o número de dias dedicados aos estudos por semana: "))
total_horas = float(input("Informe a a média de horas estudada por dia: "))
total_semana = total_dias * total_horas
curso = input("Informe o nome do curso que irá estudar: ")
print()
print(f"Olá {nome}, estudando {total_dias} dias por semana, você estuda {total_semana} horas semanais
      , assim completará rapidamente o curso de {curso}. Parabéns pela dedicação.")
print()
