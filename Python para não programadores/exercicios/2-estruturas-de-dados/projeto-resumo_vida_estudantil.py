# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e 
# imprimiremos na tela esse dados em um formato amigável.
estudante = {}
# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, 
# ano atual e os cursos realizados no LinkedIn Learning separados por virgula 
# em ordem cronológica
# 2. Armazene esses dados em um dicionário
estudante['nome'] = input("Informe seu nome: ")
estudante['ano_LinkedIn'] = int(input("Informe o ano que conheceu o LinkedIn: "))
estudante['ano_atual'] = int(input("Informe a ano atual: "))
cursos = input("Informe os cursos que estudou separados por vírgula: ")
estudante['cursos'] = cursos.split(', ')
print()

print(estudante)

print()

# 3. Imprima na tela uma string com as informações 
# de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f"Oi {estudante['nome']}, desde {estudante['ano_LinkedIn']} você conhece o LinkedIn.Nesses {estudante['ano_atual'] - estudante['ano_LinkedIn']} anos, você realizou {len(estudante['cursos'])} cursos,sendo o primeiro curso '{estudante['cursos'][0]}' e último '{estudante['cursos'][-1]}'.")