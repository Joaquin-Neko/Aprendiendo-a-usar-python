import random

dificultad = input("Facil, medio, dificil").lower()

if dificultad == "Facil":

    secreto = random.randint(1,10)

 elif dificultad == "medio":

     secreto = random.randint(1,50)

else:
    secreto = random.randint(1,100)


vida = 3

intentos = 0

while vida > 0:
    numero = int(input("Elija un numero del 1 al 10"))

    intentos += 1

    if numero == secreto:
        print("Ganaste")
        print("Ganaste en", intentos, "intentos")
        break

    elif numero > secreto:
        print("Mas bajo")

    else:
        print("Mas alto")

    vida -= 1

    print("te quedan", vida, "vidas")

if vida == 0:

    print("Perdiste")

