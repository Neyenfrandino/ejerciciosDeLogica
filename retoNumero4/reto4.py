#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
import random
from random import randint

# inforacion requeridos en variables.
numeros = [1,2,3,4,5,6,7,8,9]
letras = []
letras_mayuscucas = []

for letra in range(ord('a'), ord('z') + 1):
    letras.append(chr(letra))
    letras_mayuscucas.append(chr(letra).upper())
logitud_codigo = [8, 16]
indice_logitud = randint(8 , 16)
codigo = []

while len(codigo)< indice_logitud:
    opcion_aleatoria = random.choice([letras, numeros, letras_mayuscucas])
    elemento_aleatorio = random.choice(opcion_aleatoria)
    codigo.append(elemento_aleatorio)


codigo_unido = ''.join(map(str, codigo))
print(codigo_unido)

