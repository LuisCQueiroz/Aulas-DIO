arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula pratica')
arquivo.close()

# Leitura do arquivo texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

