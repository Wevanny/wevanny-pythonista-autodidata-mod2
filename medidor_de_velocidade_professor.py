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
- Velocidade.
2. O que devo fazer com estes dados?
- Levando em consideração a velocidade máxima permitida de 80 km/h em uma determinada rua. Crie um programa 
que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou 
uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade 
máxima seu programa deve exibir "não houve multa", caso esteja 10 km/h acima deve exibir "levou multa leve",
caso esteja entre 11 e 20 km/h acima da velocidade máxima deve exibir "levou multa grave" e caso esteja a 
mais de 20 km/h acima da velocidade máxima deverá exibir "levou multa gravíssima".
3. Quais são as restrições deste problema?
- 
4. Qual é o resultado esperado?
- O resultado esperado é exibir a mensagem que corresponde ao nível da multa que a pessoa levou (deve exibir "levou multa leve",
caso esteja entre 11 e 20 km/h acima da velocidade máxima deve exibir "levou multa grave" e caso esteja a 
mais de 20 km/h acima da velocidade máxima deverá exibir "levou multa gravíssima") 
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input velocidade
velocidade_maxima = 80
if velocidade_do_usuario <= velocidade_maxima
    print "Não levou multa"    
if velocidade > velocidade_maxima e velocidade_do_usuario <= velocidade_maxima_permitida + 10:
    print "Levou multa leve"  
if velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima_permitida + 20:
    print "Levou multa grave"
if velocidade > velocidade_maxima + 21
    print "Levou multa gravíssima"
'''
velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não houve multa.')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve.')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave.')
elif velocidade >= velocidade_maxima + 21:
    print('Levou multa gravíssima.')