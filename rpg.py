import random

atacar_enemigo = 1

curarse_enemigo = 2

vida = 30

vida_enemigo = 20

while vida > 0 and vida_enemigo > 0:

    acciones = input("atacar o curarse:").lower()

    if acciones == "atacar":

        atacar = random.randint(5,10)

        vida_enemigo -= atacar
        
        print("Atacaste al enemigo")

        print("Vida del enemigo:", vida_enemigo)

        if vida_enemigo <= 0:

            print("Ganaste")

            break

    else:

        curarse = random.randint(3,7)

        vida += curarse

        print("Te curaste")

        print("Tu vida:", vida)

    acciones_enemigo = random.randint(1,2)

    if acciones_enemigo == 1:

        daño_enemigo = random.randint(5,10)
        
        vida -= daño_enemigo
        
        print("El enemigo ataco")

        print("Tu vida:", vida)

    else:

        curacion_enemiga = random.randint(3,7)

        vida_enemigo += curacion_enemiga

        print("El enemigo se curo")

        print("Vida del enemigo:", vida_enemigo)
