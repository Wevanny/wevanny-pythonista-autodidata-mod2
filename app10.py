# Valores aletórios com random.
import random

print(random.random()) # Gera um valor de 0.0 a 1.0.
# Gera um valor decimal de valor Mínimo ao valor Máximo.

print(random.uniform(4, 10))

print(random.randint(4, 10))

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores)) # Escolher opção aleatória.
print(random.choices(cores, k=2)) # Escolher opções aleatórias.

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_de_um_baralho)) # Embaralhar uma lista.
print(cartas_de_um_baralho)
print('---')

# DESAFIOS:
'''
Desafio 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa. Jogue as opções dentro de
uma variável e depois crie um programa que imprima 'cara' ou 'coroa' na tela.

Desafio 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes. Crie uma lista de cinco nomes e 
sorteie um nome de dentro dessa lista e exiba na tela.

Desafio 3. Você quer escolher aleatóriamente um número de 10-100. Imprima na tela um valor aleatório entre 10
e 100.
'''
moeda = ['cara', 'coroa']
print(random.choice(moeda))
print('---')

lista_de_nomes = ['Wevanny', 'Dalila', 'Liam', 'Azucrenildo', 'Elioesferivaldo']
print(random.choice(lista_de_nomes))
print('---')

print(random.randint(10, 100))