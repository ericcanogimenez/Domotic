import random
import datetime
import time
import threading

hores = 0
minuts = 0
executant_rellotge = True

def rellotge():
    global hores, minuts, executant_rellotge
    while executant_rellotge:
        time.sleep(1)
        minuts += 1
        if minuts == 60:
            minuts = 0
            hores += 1
        if hores == 24:
            hores = 0

def temps_actual():
    global hores, minuts
    return f"{hores:02d}:{minuts:02d}"

def main():
    global executant_rellotge

    thread = threading.Thread(target=rellotge, daemon=True)
    thread.start()

    print("--------------")
    print("Menu principal")
    print("--------------")
    time.sleep(1)    

    sortir = False

    while not sortir:
        print(f"\nHora simulada actual: {temps_actual()}")
        print("Què vols fer?")
        print("1. Configuració de paràmetres")
        print("2. Visualitzar simulació")
        print("3. Sortir")
        simular = input("(1, 2 o 3):")

        if simular == "1":
            opcio = input("Vols configurar el sensor o la camara? (sensor/camara): ").lower()

            if opcio == "sensor":
                sensor()
            elif opcio == "camara":
                thermal()
            else:
                print("Has d'escriure 'sensor' o 'camara'.")

        elif simular == "2":
            opcio = input("Que vols simular?\n1.Sensor de moviment\n2.Camara termica\n")
            temps = temps_actual()
            if opcio == "1":
                simulacio_sensor(temps)
            elif opcio == "2":
                simulacio_thermal(temps)
            else:
                print("Opció no vàlida.")

        elif simular == "3":
            print("Sortint del programa...")
            sortir = True
            executant_rellotge = False
            break
        else:
            print("Opció incorrecta.")

def sensor():
    print("-------------")
    print("Motion Sensor")
    print("-------------")
    time.sleep(1)

    opcio = input("El sensor (on/off): ").lower()

    if opcio == "on":
        on(opcio)
    elif opcio == "off":
        off(opcio)
    else:
        print("Has d'escriure 'on' o 'off'.")

def off(state):
    print("-----------------------")
    print(f"El sensor està {state}")
    print("-----------------------")
    time.sleep(2)

def on(state):
    print("--------------------")
    print(f"El sensor està {state}")
    print("--------------------")
    time.sleep(2)
    print("Els sensors han detectat un intrús...")

    numero = random.randint(1, 5)
    temps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if numero == 1:
        print(f"Hi ha hagut moviment en totes les habitacions: {temps}")
    elif numero == 2:
        print(f"Hi ha hagut moviment a la cuina: {temps}")
    elif numero == 3:
        print(f"Hi ha hagut moviment al bany: {temps}")
    elif numero == 4:
        print(f"Hi ha hagut moviment a l'habitació: {temps}")
    elif numero == 5:
        print(f"Hi ha hagut moviment a la sala d'espera: {temps}")

    vols = input("Vols accedir a la càmera? (si/no): ").lower()
    if vols == "si":
        print(f"Et recomano la càmera número {numero}.")
        print("Rooms\n 1. Totes les habitacions\n 2. Cuina\n 3. Bany\n 4. Habitació\n 5. Sala d'espera")
        opcio_on = int(input("Escull una càmera (1-5): "))

        if opcio_on == numero:
            gos = 4
            sort = random.randint(1, 4)
            time.sleep(1)
            if sort == gos:
                print("Has tingut sort, només era el gos!")
            else:
                print("Hi ha un lladre a casa teva!!!")
                trucar = input("Vols trucar a la policia? (si/no): ").lower()
                if trucar == "si":
                    print("La policia està en camí.")
                    print("------------------------")
                    time.sleep(2)
                else:
                    print("Bona sort...")
        else:
            print("En aquest lloc no hi ha res")
            time.sleep(2)
            si = "on"
            on(si)
    else:
        print("Has decidit no accedir a la càmera.")

def simulacio_sensor(temps):
    print("--------------------")
    print(f"El sensor està on")
    print("--------------------")
    time.sleep(2)
    print("Els sensors han detectat un intrús...")

    numero = random.randint(1, 5)

    if numero == 1:
        print(f"Hi ha hagut moviment en totes les habitacions: {temps}")
    elif numero == 2:
        print(f"Hi ha hagut moviment a la cuina: {temps}")
    elif numero == 3:
        print(f"Hi ha hagut moviment al bany: {temps}")
    elif numero == 4:
        print(f"Hi ha hagut moviment a l'habitació: {temps}")
    elif numero == 5:
        print(f"Hi ha hagut moviment a la sala d'espera: {temps}")

    vols = input("Vols accedir a la càmera? (si/no): ").lower()
    if vols == "si":
        print(f"Et recomano la càmera número {numero}.")
        print("Rooms\n 1. Totes les habitacions\n 2. Cuina\n 3. Bany\n 4. Habitació\n 5. Sala d'espera")
        opcio_on = int(input("Escull una càmera (1-5): "))

        if opcio_on == numero:
            gos = 4
            sort = random.randint(1, 4)
            time.sleep(1)
            if sort == gos:
                print("Has tingut sort, només era el gos!")
            else:
                print("Hi ha un lladre a casa teva!!!")
                trucar = input("Vols trucar a la policia? (si/no): ").lower()
                if trucar == "si":
                    print("La policia està en camí.")
                    print("------------------------")
                    time.sleep(2)
                else:
                    print("Bona sort...")
        else:
            print("En aquest lloc no hi ha res")
            time.sleep(2)
            si = "on"
            on(si)
    else:
        print("Has decidit no accedir a la càmera.")

def thermal():
    print("Thermal Camera")
    print("--------------")

    habitacions = ["Habitació", "Cuina", "Sala d'estar", "Bany", "Oficina"]
    temperatura = random.randint(18, 26)

    print("Camera control:")
    print("1. Controlar la temperatura de l'habitació")
    print("2. Escollir habitació")
    print("3. Control manual de temperatura")
    print("4. Mostrar estat actual de la càmera")
    print("5. Sortir")
    print("------------------")

    try:
        opcio = int(input("Escull una opció (1-5): "))
    except ValueError:
        print("Has d'escriure un número.")
        return

    habitacio = None

    if opcio == 1:
        habitacio = input("A quina habitació vols ajustar la temperatura?: ")
        print(f"La càmera de {habitacio} detecta temperatura ambient...")
        time.sleep(2)
        print(f"Temperatura actual: {temperatura}°C")
        if temperatura < 20:
            print("Fa fred! S'està augmentant la temperatura.")
            temperatura += random.randint(1, 3)
        elif temperatura > 25:
            print("Fa calor! S'està reduint la temperatura.")
            temperatura -= random.randint(1, 3)
        else:
            print("Temperatura estable, no cal ajustar.")
        time.sleep(2)
        print(f"Temperatura ajustada: {temperatura}°C")

    elif opcio == 2:
        print("Habitacions disponibles:")
        print("1. Habitació")
        print("2. Cuina")
        print("3. Sala d'estar")
        print("4. Bany")
        print("5. Oficina")

        try:
            sel = int(input("Escull una habitació (1-5): "))
        except ValueError:
            print("Has d'escriure un número.")
            return

        if sel == 1:
            habitacio = "Habitació"
        elif sel == 2:
            habitacio = "Cuina"
        elif sel == 3:
            habitacio = "Sala d'estar"
        elif sel == 4:
            habitacio = "Bany"
        elif sel == 5:
            habitacio = "Oficina"
        else:
            print("Opció no vàlida.")
            return

        print(f"Has escollit: {habitacio}")
        time.sleep(1)
        temperatura = random.randint(18, 26)
        print(f"La càmera de {habitacio} detecta {temperatura}°C actualment.")

    elif opcio == 3:
        habitacio = input("Introdueix el nom de l'habitació: ")
        try:
            nova = int(input("Introdueix la nova temperatura: "))
            temperatura = nova
            print(f"La temperatura de {habitacio} s'ha ajustat a {temperatura}°C.")
        except ValueError:
            print("Has d'introduir un número.")

    elif opcio == 4:
        habitacio = input("De quina habitació vols veure l'estat?: ")
        print(f"La càmera de {habitacio} mostra una temperatura de {temperatura}°C.")

    elif opcio == 5:
        print("Sortint del control de la càmera tèrmica...")
        time.sleep(1)
        return
    else:
        print("Opció no vàlida.")

def simulacio_thermal(temps):
    print("Thermal Camera")
    print("--------------")

    habitacions = ["Habitació", "Cuina", "Sala d'estar", "Bany", "Oficina"]
    temperatura = random.randint(18, 26)

    print(f"Hora de la lectura: {temps}")
    print("Lectura tèrmica realitzada correctament.")
    print(f"Temperatura detectada: {temperatura}°C")

if __name__ == "__main__":
    main()
