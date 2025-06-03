

print("Jednoduchá kalkulačka")
print("Vyber operaci:")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")

volba = input("Zadej číslo operace (1/2/3/4): ")

a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))

if volba == "1":
    vysledek = a + b
    print("Výsledek:", vysledek)
elif volba == "2":
    vysledek = a - b
    print("Výsledek:", vysledek)
elif volba == "3":
    vysledek = a * b
    print("Výsledek:", vysledek)
elif volba == "4":
    if b != 0:
        vysledek = a / b
        print("Výsledek:", vysledek)
    else:
        print("Chyba: dělení nulou není možné.")
else:
    print("Neplatná volba.")




#input() – načítání volby a čísel.

#float() – převod na desetinné číslo.

#if...elif...else – výběr operace.

#Ošetření dělení nulou (if b != 0).





