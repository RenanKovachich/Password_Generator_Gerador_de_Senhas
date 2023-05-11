import random
import string

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = '0123456789'
simbolos = "#![]{}()*;/,_-"

combinar = alfabeto_mais + alfabeto_menos + numeros + simbolos

comprimento = 10

senha = "".join(random.sample(combinar, comprimento))

print(senha)
