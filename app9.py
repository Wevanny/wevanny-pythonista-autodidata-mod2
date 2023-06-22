# Import datetime
from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print('---')

# Criar uma data
lancamento_app = datetime(2024,8,14)
print(lancamento_app)
print('---')

# Receber data de lançamento do aplicativo

data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
print(type(data_de_lancamento))
print(data_de_lancamento)
print('---')

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)
print('---')

# DESAFIO
# Calcular quantos dias faltam para meu aniversário.

aniversario = '11/07/2023'
aniversario = datetime.strptime(aniversario, '%d/%m/%Y')
hoje = datetime.now()
dias_faltantes = aniversario - hoje
print(dias_faltantes)
print('---')

# Solução do professor
aniversario2 = datetime(2023,7,11)
dias_para_aniversario = aniversario - datetime.now()
print(dias_para_aniversario)



