codigo = int(input("Digite o código do funcionário: "))
nome = input('Digite o nome do fucionário: ')
salario = float(input("Informe o salário, separando as casas decimais com ponto: "))
ativo = True

print('Código: %d'% codigo)
print('Nome: %s' % nome)
print('Salário: R$ %.2f' % salario)
print('Ativo: %r' % ativo)