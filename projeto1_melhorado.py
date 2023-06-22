'''
# PROJETO 1

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do 
funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1


1. Obtenha o nome do usuário

2. Obtenha a idade do usuário

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, 
que é sorteado de forma aleatória:

# cartoes = ['R$50,00','R$250,00','R$120,00']

5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)


## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!

Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''

# Método 5 Q's para montar um algorítimo do Módulo 1:
'''
Analise criticamente o problema e descubra(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema):

1. Quais são os dados de entrada necessários?
- Nome do usuário;
- Idade do usuário;
- Data do cadastro do usuário;
- Cartões para sorteio aleatório;
- Data de aniversário do usuário no formato dd/mm/aaaa.
2. O que devo fazer com estes dados?
- Criar um registro de funcionário com sua data de nascimento, idade, data de registro e sortear-lhe um cartão
de compras.
3. Quais são as restrições deste problema?
- O fornecimento de dados únicos para o registro é obrigatório. 
4. Qual é o resultado esperado?
- Ter os dados disponíveis para aplicação funcional no Módulo 2.
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
1º input nome_do_usuário
2º input idade_do_usuario
3º input data_de_aniversario
4º input data_do_cadastro
5º cartoes = ['R$50,00','R$250,00','R$120,00']
'''

'''from datetime import datetime
nome_do_usuario = input('Digite seu nome completo: ')
data_aniversario_registro = datetime.strptime(input('Digite sua data de nascimento: '),'%d/%m/%Y')
data_aniversario_calculo = data_aniversario_registro.date()
from datetime import date
data_de_hoje = date.today()
data_de_hoje = data_de_hoje.date()
idade = data_de_hoje - data_aniversario_calculo
print(idade)
'''
from datetime import datetime
user_name = input('Qual é o seu nome completo? ')
user_age = input('Qual é a sua idade? ')
user_birthday = datetime.strptime(input('Qual a sua data de aniversário? '), '%d/%m/%Y')
registration_date = datetime.today()
today = datetime.now()
age = today - user_birthday
print(age.days / 365)
