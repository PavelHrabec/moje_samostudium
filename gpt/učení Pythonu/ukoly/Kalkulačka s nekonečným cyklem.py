



print("Jednoduchá kalkulačka")

while True:
    print("\nVyber operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("konec - ukončit program")

    volba = input("Zadej číslo operace (1/2/3/4) nebo 'konec': ")

    if volba == "konec":
        print("Program ukončen.")
        break  # ukončí cyklus

    if volba not in ("1", "2", "3", "4"):
        print("Neplatná volba. Zkus to znovu.")
        continue  # přeskočí zbytek cyklu a začne znovu

    a = float(input("Zadej první číslo: "))
    b = float(input("Zadej druhé číslo: "))

    if volba == "1":
        print("Výsledek:", a + b)
    elif volba == "2":
        print("Výsledek:", a - b)
    elif volba == "3":
        print("Výsledek:", a * b)
    elif volba == "4":
        if b != 0:
            print("Výsledek:", a / b)
        else:
            print("Chyba: dělení nulou není možné.")


#Co je nové:
#while True: → nekonečný cyklus.

#break → ukončí cyklus.

#continue → přeskočí zbytek cyklu a skočí zpět na začátek.

#Ošetření neplatných voleb.
