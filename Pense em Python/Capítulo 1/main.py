# Utilizando o Python Como calculadora

# 1 - Quantos segundos há em 42 minutos e 42 segundos?

print("\n1 - Quantos segundos há em 42 minutos e 42 segundos?")
print("(42*60)+42")
print("Resposta: ", (42*60)+42, "segundos")
print("((42*60)+42)/(60*60)")
print(((42*60)+42)/(60*60), "horas")

# 2 - Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
print("\n2 - Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.")
print("10 / 1.61")
print("Resposta: ", 10 / 1.61, "milhas")

# 3 - Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)?
print("\n3 - Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)?")
print("(42 * 60 + 42) / (10 / 1.61) / 60")
print("Resposta:", (42 * 60 + 42) / (10 / 1.61) / 60, "é o passo médio.")

# 3.1 - Qual é a sua velocidade média em milhas por hora?
print("\n3.1 - Qual é a sua velocidade média em milhas por hora?")
print("(10 / 1.61)/(((42*60)+42)/(60*60))")
print("A velocidade é:",(10 / 1.61)/(((42*60)+42)/(60*60)),"milhas por hora")
