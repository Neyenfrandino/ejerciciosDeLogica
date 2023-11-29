# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */


import random

lista_piedra_papel_tijeras_lagarto_spock = {'tijeras': "✂️", 'piedra':"🗿", 'papel':"📄", 'lagarto':"🦎", 'spock':"🖖"}
def desarrollo_del_juego():
    numero_juegos = 0
    players = {'Player1': '', 'player2': ''}
    resultados = []

    while numero_juegos < 9:
        juego_actual = {}
        for player in players:
            clave_aleatoria = random.choice(list(lista_piedra_papel_tijeras_lagarto_spock.keys()))
            valor_aleatorio = lista_piedra_papel_tijeras_lagarto_spock[clave_aleatoria]
            juego_actual[player] = valor_aleatorio

        resultados.append(juego_actual)
        numero_juegos += 1
    return resultados


def obtener_resultado_del_juego():
    resultados = desarrollo_del_juego()

    player1 = 0
    player2 = 0

    # Obtener el valor de cada juego
    for juego in resultados:
        print(f"Juego: {juego}")

        jugador1 = juego.get('Player1', '')
        jugador2 = juego.get('player2', '')

        if jugador1 == jugador2:
            print("Empate!")
        elif (
            (jugador1 == "🗿" and (jugador2 == "✂️" or jugador2 == "🦎")) or
            (jugador1 == "✂️" and (jugador2 == "📄" or jugador2 == "🦎")) or
            (jugador1 == "🖖" and (jugador2 == "🗿" or jugador2 == "✂️")) or
            (jugador1 == "🦎" and (jugador2 == "🖖" or jugador2 == "📄")) or
            (jugador1 == "📄" and (jugador2 == "🗿" or jugador2 == "🖖"))
        ):
            print("Player1 gana!")
            player1 += 1
        else:
            print("player2 gana!")
            player2 += 1

    print("Puntajes finales:")
    print("Player1:", player1)
    print("player2:", player2)

obtener_resultado_del_juego()



