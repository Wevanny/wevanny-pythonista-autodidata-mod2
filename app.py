velocidade_internet = 10
print(velocidade_internet)
# Quais tipos de dados podemos armazenar na memória o computador?
# Números:
velocidade_internet = 10
# Valores booleanos:
esta_aberta = True
# Strings:
slogan = 'Feito é mellhor que perfeito!'
slogan = "Feito é melhor que perfeito!"
# São os chamados Tipos Primitivos.
# É possível fazer mais de uma atribuição por vez (unpacking).
a,b,c,d = 1,2,3,4
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(velocidade_internet))
print(type(b), type(esta_aberta))
print('----------')
# Desafio! 
# Copie e cole as seguintes linhas de código para seu editor de código e descubra qual é o tipo de cada um desses dados:
variavel_1 = 25.87
print(type(variavel_1))
variavel_2 = True
print(type(variavel_2))
variavel_3 = 'Bom dia!'
variavel_4 = 15
print(type(variavel_3), type(variavel_4))

#  Como resolver QUALQUER erro com GOOGLE ou CHATGPT
# Erro Genérico:
'''
1. Leia o erro;
2. Se não souber inglês copie a mensagem e cole no Google Tradutor;
3. Tente entender o que fazer a partir da mensagem;
4. Pesquisar no Google(colocando 'Python' antes do erro).
OU
1. Acessando o CHATGPT e digitando "Como resolver o erro de Python: 'Digitar o erro aqui';
2. Colando o erro em inglês no CHATGPT.
'''
nome = 'Amanda'
       #012345
#print(nome[6]) --> IndexError: string index out of range
print(nome[5])

# Erro Específico(inclui dados da sua aplicação):
'''
1. Leia o erro;
2. Copie somente a parte genérica do erro;
2. Se não souber inglês cole a mensagem no Google Tradutor;
3. Tente entender o que fazer a partir da mensagem;
4. Pesquisar no Google(colocando 'Python' antes do erro).
OU
1. Acessando o CHATGPT e digitando "Como resolver o erro de Python: 'Digitar o erro aqui';
2. Colando o erro em inglês no CHATGPT.
'''
with open('senhas.txt', 'r') as arquivo: 
    for linha in arquivo:
        print(linha)
# --> Erro apresentado antes da correção: FileNotFoundError: [Errno 2] No such file or directory: 'senhas.txt'.