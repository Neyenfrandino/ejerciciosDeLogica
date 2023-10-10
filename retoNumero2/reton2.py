# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opcóin de cada transformación. Por ejemplo "4" para la "a")
#  */
alfabeto = {'a':'4',
            'b':'|3',
            'c':'[',
            'd':')',
            'e':'3',
            'f':'|=',
            'g':'&',
            'h':'#',
            'i':'1',
            'j':',_|',
            'k':'>|',
            'l':'1',
            'm':'/\/',
            'n':'^/',
            'o':'0',
            'p':'|*',
            'q':'(_,)',
            'r':'I2',
            's':'5',
            't':'7',
            'u':'(_)',
            'v':'\/',
            'w':'\/\/',
            'x':'><',
            'y':'j',
            'z':'2',
            ' ': ' '}

palabara_usuario = input('Dime algo: ').lower()
valor_alfabeto = ''
for letra in palabara_usuario:
    valor_alfabeto += alfabeto[letra]
print(valor_alfabeto)









