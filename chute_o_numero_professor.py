''' Escreva um programa que ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um 
número até que o valor chutado seja igual ao gerado aleatoriamente.
    O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do 
programa.

Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema):

1. Quais são os dados de entrada necessários?
- Valor aleatório de 1 a 10.
- Chute do usuário.
2. O que devo fazer com estes dados?
- Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início do programa e dizer se 
o chute foi maior, menor ou igual ao valor que foi gerado no início do programa.
3. Quais são as restrições deste problema?
- Um valor aleatório de 1 a 10. 
4. Qual é o resultado esperado?
- O resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório
gerado no início do programa.
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
    print "Chute foi maior que o valor gerado."
if chute < valor_aleatorio
    print "Chute foi menor que o valor gerado."    
if chute = valor_aleatorio:
    print "Você acertou!"
'''

import random
valor_aleatorio = random.randint(1, 10)
print(valor_aleatorio)
#chute = int(input('Chute um valor de 1 a 10:'))
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10:'))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado.')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado.')
    elif chute == valor_aleatorio:
        print('você acertou!')