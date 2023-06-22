teclado = 'Teclado'
print(teclado[2])
print(teclado[4])
print('---')

teclado2 = 'Teclado Teclado Teclado Teclado Teclado'
print(teclado2[-1])
print(teclado2.index('l'))
print(teclado2[teclado2.index('l')])
print('---')

# Acessando partes de uma string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])
print('---')

frase = 'Clean Code'
print(frase.rindex('C'))
print('---')

# DESAFIO 1:
# Encontre o índice de 'o' da variável biblioteca:
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))
print(biblioteca[biblioteca.index('o')])
print('---')

# DESAFIO 2:
# Usando as palavras 'Desenvolvimento de Aplicações' imprima  apenas as palavras 'de Aplicações':
string = 'Desenvolvimento de Aplicações'
print(string[string.index('d'):])
print(string[-13:])
# Resposta do professor:
indice_d = string.rindex('d')
indice_s = string.rindex('s')
print(string[indice_d:indice_s+1])




      
