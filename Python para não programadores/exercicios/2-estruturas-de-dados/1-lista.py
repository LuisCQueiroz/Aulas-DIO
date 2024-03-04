# Crie uma lista apenas com elementos numéricos
print("Crie uma lista apenas com elementos numéricos")
lista1 = [1,2,3,4,5]
print(type(lista1))
print("Lista numérica", lista1)
print()
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
print("Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora")
list2 =[1,2,"String", 2.5,True, False, ["João", "Maria", "José", 1, 2, 3]]
print(type(list2))
print(list2)
print()
# Imprima na tela apenas os 5 primeiros elementos da lista
print("Imprima na tela apenas os 5 primeiros elementos da lista anterior")
print(list2[:5])
print()
# Crie um slice na lista para que imprima na tela os elementos de índice par
print("Crie um slice na lista para que imprima na tela os elementos de índice par")
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista3)
# slice[inicio, fim, passo] se não souber o último número da lista utilize -1
print(lista3[1:11:2])
print()
# Remova da lista o último item
print("Remova da lista o último item")
print(lista3)
lista3.pop()
print(lista3)
print()
# Insira na lista um novo item
print("Insira na lista um novo item")
list4 = []
print(list4)
list4.extend(lista3) # Adiciona elementos a partir de outra lista
lista3.append(12)
print(lista3)
print(list4)
# Remova da lista um item específico
print("Remova da lista um item específico - item 9")
lista3.remove(9)
print(lista3)