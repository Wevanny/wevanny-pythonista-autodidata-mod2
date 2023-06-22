termo = int(input('Digite um número para obter o Fatorial:'))
if termo <= 0:
    print('O número adotado será 1 pois o cálculo do fatorial exige um número positivo maior que zero.')
    termo = 1
numero = termo
fatorial = 1
for i in range(termo):
    fatorial = fatorial * numero
    numero = numero - 1
print(fatorial)