




import random

tajne_cislo = random.randint(1, 10)

max_pokusy = 5
pokusy = 0

while pokusy < max_pokusy:
    tip = int(input("Hádej číslo od 1 do 10:"))
    pokusy += 1



    if tip == tajne_cislo:
        print(f"Uhodl jsi to na {pokusy}. pokus! Číslo bylo {tajne_cislo}.")
        break
    elif tip < tajne_cislo:
        print("Moc malé.")
    else:
        print("Moc velké.")

if pokusy == max_pokusy and tip != tajne_cislo:
    print(f"Prohrál jsi!Číslo bylo {tajne_cislo}.")

















