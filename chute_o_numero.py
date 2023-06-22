''' Escreva um programa que ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um 
número até que o valor chutado seja igual ao gerado aleatoriamente.
    O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do 
programa.

Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema):

1. Quais são os dados de entrada necessários?
Número aleatório e chute do usuário.
2. O que devo fazer com estes dados?
Compará-los e retornar se são iguais ou se o chute é maior ou menor que o aleatório.
3. Quais são as restrições deste problema?
- Deve ser um número de 1 a 10
- O programa não deve parar até que os números sejam iguais. 
4. Qual é o resultado esperado?
Que o programa exiba se o chute foi de número mais alto ou mais baixo que o aleatório e continue pedindo 
ou que informe que o usuário acertou o chute e encerre a execução.
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input numero_aleatorio
input chute_do_usuario
while chute = False
if numero_aleatorio == chute_do_usuario
    print você acertou
    chute = True
else if numero_aleatorio > chute_do_usuario
    print chute foi mais alto
else
    print chute foi mais baixo
'''

import random
aleatorio = random.randint(1, 10)
print(aleatorio)
chute_do_usuario = int(input('Chute um número de 1 a 10: '))
chute = False
while chute == False:
    if chute_do_usuario == aleatorio:
        print('Você acertou!')
        chute = True
    elif chute_do_usuario > aleatorio: 
        print('O chute foi mais alto que o número alvo!')
        chute_do_usuario = int(input('Chute um número de 1 a 10: '))
    elif chute_do_usuario < aleatorio: 
        print('O chute foi mais baixo que o número alvo!')
        chute_do_usuario = int(input('Chute um número de 1 a 10: '))