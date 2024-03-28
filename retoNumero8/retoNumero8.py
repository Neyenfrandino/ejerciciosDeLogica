
##Crea 3 funciones, cada una encargada de detectar si una cadena de
##texto es un heterograma, un isograma o un pangrama.
## Debes buscar la definición de cada uno de estos términos.


##Heterograma:(Un heterograma es una palabra que no tiene ninguna letra repetida.)
# "Jovencillo emponzoñado de whisky, qué mala figurota exhibes."


##Pangrama: (Esta frase incluye todas las letras del alfabeto español al menos una vez)
## = "El veloz murciélago hindú comía feliz cardillo y kiwi."

texto = 'Adulterinos'
def isograma (text) :
    acount_letter = ''
    join_text = text.replace(" ", "")
    for i in (range(ord('a'), ord('z') + 1)):
        if join_text.count(chr(i)) == 1:
            acount_letter += chr(i)

    if len(acount_letter) == len(join_text):
        print(f'Soy un Heterograma "{text.upper()}" ')

    else:
        print(f'No soy un Heterograma: {text}')
        return


isograma(texto.lower())