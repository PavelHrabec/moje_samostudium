


import random

tajne_cislo = random.randint(1, 10)  # Vygeneruje číslo od 1 do 10
pokus = 0
uhodnuto = False

print("Hádej číslo od 1 do 10.")

while not uhodnuto:
    tip = int(input("Tvůj tip: "))
    pokus += 1

    if tip < tajne_cislo:
        print("Moc malé!")
    elif tip > tajne_cislo:
        print("Moc velké!")
    else:
        print("Správně! Uhodl(a) jsi číslo za", pokus, "pokusů.")
        uhodnuto = True



#Co se tu učíš:
#import random – používáme knihovnu pro náhodná čísla.

#while not uhodnuto – cyklus běží, dokud hráč neuhodne číslo.

#if, elif, else – porovnávání hodnot.

#input() – načtení vstupu od hráče.

#int() – převod vstupu na celé číslo.



