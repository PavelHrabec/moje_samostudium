

def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

def nasob(a, b):
    return a * b

def deleni(a, b):
    if b != 0:
        return a / b
    else:
        return "Chyba: dělení nulou není možné."

def vypocet(volba, a, b):
    if volba == "1":
        return secti(a, b)
    elif volba == "2":
        return odecti(a, b)
    elif volba == "3":
        return nasob(a, b)
    elif volba == "4":
        return deleni(a, b)
    else:
        return "Neplatná volba."

def zobraz_menu():
    print("\nVyber operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("konec - ukončit program")

def hlavni_program():
    print("Jednoduchá kalkulačka s funkcemi")
    while True:
        zobraz_menu()
        volba = input("Zadej operaci: ")

        if volba == "konec":
            print("Program ukončen.")
            break

        if volba not in ("1", "2", "3", "4"):
            print("Neplatná volba. Zkus to znovu.")
            continue

        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
        vysledek = vypocet(volba, a, b)
        print("Výsledek:", vysledek)

# Spuštění programu
hlavni_program()


#Co ses právě naučil:
#Definování funkcí pomocí def.

#Funkce vrací výsledek pomocí return.

#Hlavní logiku programu jsme přesunuli do hlavni_program() – to je běžná praxe.

#Každá část kódu má teď svůj jasný účel.



