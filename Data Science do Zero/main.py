from collections import Counter
from collections import defaultdict

import matplotlib
import matplotlib.pyplot as plt


# Criando um data Dump - Lista de  Usuários
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]
# Criando pares de  amizades
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# inicializando um dicionário com uma lista vazia para cada id de usuário
friendships = {user["id"]: [] for user in users}

# utilizando loop pelos pares de amigos para preenche-la
for i, j in friendship_pairs:
    friendships[i].append(j)  # Adicione j como amigo do usuário i
    friendships[j].append(i)  # Adicione i como amigo do usuário j

def number_of_friends(user):
    # Quantos amigos tem o usuário
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)                              # tamanho da lista de usuários
avg_connections = total_connections / num_users     # 24/10 == 2,4

print(total_connections)
print(num_users)
print(avg_connections, "\n")

# Criando uma lista (user_id, number of friends) organizada por ID
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

print(num_friends_by_id)

def foaf_ids_bad(user):
    """foaf significa "friend os a fried (amigo de um amigo)"""
    return [foaf_id for friend_id in friendships[user["id"]] for foaf_id in friendships[friend_id]]

"""Imprimindo os amigos do amigo 0"""
print("\nAmigos de um Amigo")
print(foaf_ids_bad(users[0]))
print("Resumo: O user 0 possui dois amigos 1 e 2, seu amigos foram impressos\n")

print("Amigos do usuário 0: ", friendships[0])
print("Amigos do usuário 1: ", friendships[1])
print("Amigos do usuário 2: ", friendships[2])
print("Amigos do usuário 3: ", friendships[3])
print("Amigos do usuário 4: ", friendships[4])
print("Amigos do usuário 5: ", friendships[5])
print("Amigos do usuário 6: ", friendships[6])
print("Amigos do usuário 7: ", friendships[7])
print("Amigos do usuário 8: ", friendships[8])
print("Amigos do usuário 9: ", friendships[9])


print("\nVerificando quantos amigos o 3 tem em comum com o 0 e os que sejam em comum mas não tenam em comum o do 0.")
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]           # Para cada amigo meu,
        for foaf_id in friendships[friend_id]           # encontre os amigos deles
        if foaf_id != user_id                           # que não seja eu
        and foaf_id not in friendships[user_id]         # e não sejam meus amigos
         )
print(friends_of_friends(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (2, "R"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvn"),
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data"), (9, "Cassandra")
]

def data_scientists_who_like(target_interest):
    """Encontre o ids dos usuários com o mesmo interesse"""
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]

print("\nEncontre o ids dos usuários com o mesmo interesse")
print(data_scientists_who_like("Cassandra"))

# As chaves são interesses, os valores são listas de user_ids com o interesse em gestão
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print("\nInteresses e seus Usuários")
print(user_ids_by_interest)

# As chaves são user_ids, os valores são listas de interesses do user_id em questão
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

print("\nUsuários e seus interesses")
print(interests_by_user_id)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print("\nUsuários e quantidade de interesses em comum")
print(most_common_interests_with(users[2]))

# Salários e Experiência
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

"""plt.scatter(salaries_and_tenures[0][1], salaries_and_tenures[0][0])
plt.scatter(salaries_and_tenures[1][1], salaries_and_tenures[1][0])
plt.scatter(salaries_and_tenures[2][1], salaries_and_tenures[2][0])
plt.scatter(salaries_and_tenures[3][1], salaries_and_tenures[3][0])
plt.scatter(salaries_and_tenures[4][1], salaries_and_tenures[4][0])
plt.scatter(salaries_and_tenures[5][1], salaries_and_tenures[5][0])
plt.scatter(salaries_and_tenures[6][1], salaries_and_tenures[6][0])
plt.scatter(salaries_and_tenures[7][1], salaries_and_tenures[7][0])
plt.scatter(salaries_and_tenures[8][1], salaries_and_tenures[8][0])
plt.scatter(salaries_and_tenures[9][1], salaries_and_tenures[9][0])"""

x = 0
while (x < 10):
    plt.scatter(salaries_and_tenures[x][1], salaries_and_tenures[x][0])
    x = x + 1

matplotlib.pyplot.title('Salários e Experiência')
matplotlib.pyplot.xlabel('Experiência')
matplotlib.pyplot.ylabel('Salários em R$')

# matplotlib.pyplot.plot(salaries_and_tenures) - Grafico de linhas
plt.show()

# As chaves são anos, os valores são listas de salários por anos de experiência.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print("\nValores por anos de experiência:")
print(salary_by_tenure)

# As chaves são anos, cada valor é o salário médio associado ao número de anos de experiência.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print("\nMédia dos salários por anos de experiência:")
print(average_salary_by_tenure)

print("\nBuckets de anos de experiência")
def tenure_bucket(tenure):
    if tenure < 2:
        return "Menor que dois"
    elif tenure < 5:
        return "Entre dois e cinco"
    else:
        return "Mais que cinco"
print(tenure_bucket(tenure))