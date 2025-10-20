import time
import datetime

nom = ""
edat = 0
pes = 0.0
alçada = 0.0

while True:
    print("-----------------------------")
    print("            Menu             ")
    print("-----------------------------")

    opcio = input("Què vols fer?\n 1. Introduir dades\n 2. Modificar dades\n 3. Visualitzar dades\n 4. Càlcul i visualització de paràmetres\n 5. Sortir\n  ")

    try:
        opcio = int(opcio)
    except ValueError:
        print("Has d'introduir un número del 1 al 5.")
        continue

    match opcio:
        # -------------------
        case 1:  # Introduir dades
            print("-----------------------------")
            print("      Introduir Dades        ")
            print("-----------------------------")

            # Nom
            while True:
                try:
                    nom_input = input("Nom complet: ").strip()
                    if not nom_input:
                        raise ValueError("El nom no pot estar buit")
                    parts = nom_input.split()
                    if not all(part.isalpha() for part in parts):
                        raise ValueError("El nom només pot contenir lletres (sense números ni símbols)")
                    if nom_input != nom_input[0].upper() + nom_input[1:]:
                        print("La primera lletra ha de ser en majúscula")
                    nom = nom_input
                    break
                except ValueError as e:
                    print(e)

            # Edat
            while True:
                try:
                    edat_input = input("Edat: ").strip()
                    if not edat_input.isdigit():
                        raise ValueError("L'edat només pot contenir números")
                    edat_int = int(edat_input)
                    if edat_int < 0:
                        raise ValueError("Has d'introduir un número positiu")
                    elif edat_int > 120:
                        raise ValueError("Edat invàlida")
                    edat = edat_int
                    break
                except ValueError as e:
                    print(e)

            # Pes
            while True:
                pes_input = input("Pes (kg): ").strip()
                if not pes_input:
                    print("El pes no pot estar buit")
                    continue
                try:
                    pes_float = float(pes_input)
                    if pes_float <= 0 or pes_float > 400:
                        print("El pes ha de ser positiu i menor o igual a 400 kg")
                        continue
                    pes = pes_float
                    break
                except ValueError:
                    print("El pes només pot contenir números i punts decimals")

            # Alçada
            while True:
                alçada_input = input("Alçada (m): ").strip()
                if not alçada_input:
                    print("Has d'afegir un valor")
                    continue
                try:
                    alçada_float = float(alçada_input)
                    if alçada_float < 0.5 or alçada_float > 2.5:
                        print("L'alçada ha de ser entre 0.5 m i 2.5 m")
                        continue
                    alçada = alçada_float
                    break
                except ValueError:
                    print("L'alçada només pot contenir números i punts decimals")

            input("\n=========== Prem ENTER per tornar al menú ===========")

        # -------------------
        case 2:  # Modificar dades
            print("-----------------------------")
            print("      Modificar dades        ")
            print("-----------------------------")
            subopcio = input("Quina dada vols modificar?\n 1. Nom complet\n 2. Edat\n 3. Pes(kg)\n 4. Alçada(m)\n ")
            try:
                subopcio = int(subopcio)
            except ValueError:
                print("Has d'introduir un número del 1 al 4.")
                continue

            match subopcio:
                case 1:  # Modificar nom
                    while True:
                        try:
                            nom_input = input(f"Nom actual ({nom}): ").strip()
                            if not nom_input:
                                raise ValueError("El nom no pot estar buit")
                            parts = nom_input.split()
                            if not all(part.isalpha() for part in parts):
                                raise ValueError("El nom només pot contenir lletres")
                            if nom_input != nom_input[0].upper() + nom_input[1:]:
                                print("La primera lletra ha de ser en majúscula")
                            nom = nom_input
                            break
                        except ValueError as e:
                            print(e)

                case 2:  # Modificar edat
                    while True:
                        try:
                            edat_input = input(f"Edat actual ({edat}): ").strip()
                            if not edat_input.isdigit():
                                raise ValueError("L'edat només pot contenir números")
                            edat_int = int(edat_input)
                            if edat_int < 0:
                                raise ValueError("Has d'introduir un número positiu")
                            elif edat_int > 120:
                                raise ValueError("Edat invàlida")
                            edat = edat_int
                            break
                        except ValueError as e:
                            print(e)

                case 3:  # Modificar pes
                    while True:
                        pes_input = input(f"Pes actual ({pes}): ").strip()
                        if not pes_input:
                            print("El pes no pot estar buit")
                            continue
                        try:
                            pes_float = float(pes_input)
                            if pes_float <= 0 or pes_float > 400:
                                print("El pes ha de ser positiu i menor o igual a 400 kg")
                                continue
                            pes = pes_float
                            break
                        except ValueError:
                            print("El pes només pot contenir números i punts decimals")

                case 4:  # Modificar alçada
                    while True:
                        alçada_input = input(f"Alçada actual ({alçada}): ").strip()
                        if not alçada_input:
                            print("Has d'afegir un valor")
                            continue
                        try:
                            alçada_float = float(alçada_input)
                            if alçada_float < 0.5 or alçada_float > 2.5:
                                print("L'alçada ha de ser entre 0.5 m i 2.5 m")
                                continue
                            alçada = alçada_float
                            break
                        except ValueError:
                            print("L'alçada només pot contenir números i punts decimals")

            input("\n=========== Prem ENTER per tornar al menú ===========")

        # -------------------
        case 3:  # Visualitzar dades
            print("-----------------------------")
            print("      Visualitzar dades      ")
            print("-----------------------------")
            if not nom:
                print("No s'han introduït dades.")
            else:
                print(f"Nom: {nom}")
                print(f"Edat: {edat}")
                print(f"Pes: {pes:.2f} kg")
                print(f"Alçada: {alçada:.2f} m")
            input("\n=========== Prem ENTER per tornar al menú ===========")

        # -------------------
        case 4:  # Càlcul i visualització de paràmetres
            if not nom:
                print("No hi ha dades introduïdes.")
                input("\n=========== Prem ENTER per tornar al menú ===========")
                continue

            print("-----------------------------")
            print("      Paràmetres calculats   ")
            print("-----------------------------")

            # Normalitzar nom
            nom_normalitzat = " ".join([part.capitalize() for part in nom.split()])

            # IMC
            imc = pes / (alçada ** 2)
            if imc < 18.5:
                categoria = "pes baix"
            elif imc < 25:
                categoria = "pes normal"
            elif imc < 30:
                categoria = "sobrepès"
            else:
                categoria = "obesitat"

            # Freqüència cardíaca
            fc_max = 220 - edat
            fc50 = round(fc_max * 0.50)
            fc85 = round(fc_max * 0.85)

            # Aigua recomanada
            aigua_l = pes * 0.035

            # Any de naixement aproximat
            any_actual = datetime.datetime.now().year
            any_naix = any_actual - edat

            # Mostrar resultats
            print(f"Hola, {nom_normalitzat}!")
            print(f"Edat: {edat} anys | Pes: {pes:.2f} kg | Alçada: {alçada:.2f} m")
            print(f"IMC: {imc:.2f} ({categoria})")
            print(f"FC màxima estimada: {fc_max} bpm")
            print(f"Zona FC objectiu: {fc50}-{fc85} bpm")
            print(f"Aigua recomanada: {aigua_l:.2f} L/dia")
            print(f"Any de naixement aproximat: {any_naix}")
            input("\n=========== Prem ENTER per tornar al menú ===========")

        # -------------------
        case 5:  # Sortir
            print("Sortint del programa...")
            time.sleep(1)
            break

        case _:  # Opció invàlida
            print("Opció invàlida. Tria un número del 1 al 5.")
