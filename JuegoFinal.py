#crear la pantalla inicial del juego 

print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
print( "╔═════════════════════════════════════╗")
print(f"║            WELCOME TO               ║")
print(f"║    PIEDRA👊, PAPEL✋, TIJERA✌️       ║")
print(f"╚═════════════════════════════════════╝")
print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")

#usuario y contraseña
#usuario = JorgeLuis
#contraseña = 2020

#ingresar el usuario y contraseña para entrar al juego

USER = str(input("ingrese el usuario: "))
PASSWORD = int(input("ingrese la contraseña: "))


if (USER == "JorgeLuis"):
    if (PASSWORD == 2020):
        print("acceso correcto")
    else:
        print("contraseña incorrecta")
else:
    print("usuario incorrecto")


#importamos una libreria para que escoja aleatoriamente las variables

import random

#interface de bienvenida

opciones = ["piedra", "papel", "tijera"]
print(f"╔═════════════════════════════════════╗")
print(f"║   ......BIENVENIDO AL JUEGO......   ║")
print(f"║      ♣ESCOJA...👊...✋...✌️          ║")
print(f"║       💻 Y GANAME SI PUEDES         ║")
print(f"╚═════════════════════════════════════╝")

#Bucle principal del juego

while True:
    jugador = input("ESCOJA: ")
    if jugador not in opciones:
        print("opciones no valida. intente de nuevo")
        continue

    computadora = random.choice(opciones)
    print(f"💻La computadora eligio {computadora}")

    if jugador == computadora:
        print("!EMPATE¡ 🥶")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("GANASTE 🥂")
    else:
        print("PERDISTE 💩")

#

    continuar = input("¿quieres jugar otras ves? ( 1 = SI, 2 = NO):")
    if continuar != "1":
       print()
       print("Gracias por jugar. !Hasta la proxima¡ 😁")
       break

