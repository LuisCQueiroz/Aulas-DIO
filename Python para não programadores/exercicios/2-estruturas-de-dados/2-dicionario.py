pessoa = {'nome':'Crislaine', 
          'idade':46, 
          'ano_formatura':2010, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['nadar', 'ler', 'pedalar'], 
          'animal_estimacao':False}

# Imprima na tela o valor equivalente a chave "hobby"
print(f"\nHobbies de {pessoa['nome']} são {pessoa['hobby']}\n")

# Imprima na tela uma lista apenas com os valores do dicionário
print("\nValores do dicionário: ",pessoa.values(), "\n")

# Imprima na tela uma lista apenas com as chaves do dicionário
print("\nChaves do dicionário: ",pessoa.keys(), "\n")

# Insira um novo par chave-valor no dicionário
pessoa['Time do coração'] = 'Corinthians'
print("\nDicionário", pessoa)
