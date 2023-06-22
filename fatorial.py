# Crie um programa que recebe um número e imprime o seu fatorial:
# Método 5 Q's para montar um algorítimo:
'''
Analise criticamente o problema e descubra(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema):

1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

1. Número para a obtenção do Fatorial.
2. Calcular o Fatorial deste do número dado.
3. O número deve ser inteiro positivo maior que zero.
4. O Fatorial do número.
5. input numero
   if numero <= 0 
   fatorial = 1
   cont = 1
   loop 0 a numero
   fatorial = fatorial * cont
   cont = cont + 1
   print fatorial    
'''
import sys  
termo = 0
if termo <= 0:    
    sys.exit('Digite apenas números inteiros positivos maiores que zero.')            
fatorial = 1
cont = 1
for i in range(termo):    
    fatorial = fatorial * cont
    cont = cont + 1
print(fatorial)        