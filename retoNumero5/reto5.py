# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */


def numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return f'{numero} no es un numero primo'
    return f'{numero} es un numero primo'

def numero_par_impar(num):
    numero_par_impar = num % 2
    if numero_par_impar == 0:
        return f'{num} es un numero par'
    else:
        return f'{num} es un numero impar'


def fibonacci(n):
    n = n + 1
    if n <= 0:
        return 'El numero debe ser positivo para calcular la secuencia de Fibonacci'
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        f = [0, 1]
        for i in range(2, n):
            next_number = f[i - 1] + f[i - 2]
            f.append(next_number)

        if n - 1 < len(f):
            return f'{n} entra en la secuencia de Fibonacci: {f[n-1]}'
        else:
            return f'{n} no entra en la secuencia de Fibonacci'

def resultado(num):
    secuencia_de_fibonacci = fibonacci(num)
    numero_es_primo = numero_primo(num)
    par_impar = numero_par_impar(num)


    print(f'{numero_es_primo}, {par_impar}, {secuencia_de_fibonacci}')


resultado(19)