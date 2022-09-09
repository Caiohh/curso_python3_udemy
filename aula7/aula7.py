nome = 'Caio Lemes'
idade = 20
altura = 1.74
e_maior = idade > 18
peso = 75
imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))