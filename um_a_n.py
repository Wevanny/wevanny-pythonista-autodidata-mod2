# Problema um a n: Imprima os valores de um a n.

'''
input numero_maximo
valor_inicial = 1
loop de valor_inicial a numero_maximo
print valor
'''

numero_maximo = int(input('Digite o número máximo:'))
valor_inicial = 1
for numero in range(valor_inicial, numero_maximo + 1):
    print(numero)
