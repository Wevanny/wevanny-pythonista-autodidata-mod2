'''
Projeto - Medidor de Multa po Velocidade:
   
   Levando em consideração a velocidade máxima permitida de 80 km/h em uma determinada rua. Crie um programa 
que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou 
uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade 
máxima seu programa deve exibir "não houve multa", caso esteja 10 km/h acima deve exibir "levou multa leve",
caso esteja entre 11 e 20 km/h acima da velocidade máxima deve exibir "levou multa grave" e caso esteja a 
mais de 20 km/h acima da velocidade máxima deverá exibir "levou multa gravíssima".

Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema):

1. Quais são os dados de entrada necessários?
- Velocidade fornecida pelo usuário.
2. O que devo fazer com estes dados?
- Compará-lo a velocidade máxima permitida e retornar a informação concernente.
3. Quais são as restrições deste problema?
- Número inteiro positivo 
4. Qual é o resultado esperado?
- Que o programa exiba se foi recebida multa ou não e se sim qual a sua gravidade. 
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input velocidade_do_usuario
velocidade_maxima_permitida = 80
if velocidade_do_usuario <= velocidade_maxima_permitida
    print Não houve multa    
else velocidade_do_usuario > velocidade_maxima_permitida e velocidade_do_usuario <= velocidade_maxima_permitida + 10
    print Levou multa leve  
else velocidade_do_usuario >= velocidade_maxima_permitida + 11 e velocidade_do_usuario <= velocidade_maxima_permitida + 20
    print Levou multa grave
else velocidade_do_usuario > velocidade_maxima_permitida + 21
    print Levou multa gravíssima
'''
velocidade_do_usuario = int(input('Digite sua velocidade: '))
velocidade_maxima_permitida = 80
if velocidade_do_usuario <= velocidade_maxima_permitida:
    print('Não houve multa.')
elif velocidade_do_usuario > velocidade_maxima_permitida and velocidade_do_usuario <= velocidade_maxima_permitida + 10:
    print('Levou multa leve.')
elif velocidade_do_usuario >= velocidade_maxima_permitida + 11 and velocidade_do_usuario <= velocidade_maxima_permitida + 20:
    print('Levou multa grave.')
elif velocidade_do_usuario >= velocidade_maxima_permitida + 21:
    print('Levou multa gravíssima.')