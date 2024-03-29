
##Crea 3 funciones, cada una encargada de detectar si una cadena de
##texto es un heterograma, un isograma o un pangrama.
## Debes buscar la definición de cada uno de estos términos.


##Heterograma:(Un heterograma es una palabra que no tiene ninguna letra repetida.)
# "Jovencillo emponzoñado de whisky, qué mala figurota exhibes."

##Isograma: (Esta palabra no tiene letras repetidas) = "Paralelepípedo"

##Pangrama: (Esta frase incluye todas las letras del alfabeto español al menos una vez)
## = "El veloz murciélago hindú comía feliz cardillo y kiwi."

texto = 'Adulterinos'
def heterograma (text) :
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


heterograma(texto.lower())



def isograma (frase):
    join_text = frase.replace(" ", "")
    for i in (range(ord('a'), ord('z') + 1)):
        if join_text.count(chr(i)) != 1:
            print(f'Soy un isograma {frase.upper()}' )
            return
        else:
            print(f'No soy un isograma {frase.upper()}')
            return

isograma('Paralelepípedo')


def pangrama(palabra):
    abcdario = ''
    join_text = palabra.replace(" ", "")

    for i in (range(ord('a'), ord('z') + 1 )):
        if chr(i) in join_text:
            abcdario += chr(i)

    if len(abcdario) == 26 :
        print(f'Soy un pangrama: "{palabra.upper()}"')
    else:
        print(f'No soy un pangrama: "{palabra.upper()}"')

pangrama("The quick brown fox jumps over the lazy dog.")