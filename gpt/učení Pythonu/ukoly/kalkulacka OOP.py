
#Co je OOP v kostce:
#Třída (class) = šablona pro objekt (např. kalkulačka).

#Objekt = konkrétní instance třídy.

#Metoda = funkce uvnitř třídy.

#self = odkaz na konkrétní objekt (jako „já“ v češtině).

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Chyba: dělení nulou není možné."

def zobraz_menu():
    print("\nVyber operaci:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("konec - ukončit program")

def hlavni_program():
    kalkulacka = Calculator()
    print("Objektově orientovaná kalkulačka")

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

        if volba == "1":
            vysledek = kalkulacka.add(a, b)
        elif volba == "2":
            vysledek = kalkulacka.subtract(a, b)
        elif volba == "3":
            vysledek = kalkulacka.multiply(a, b)
        elif volba == "4":
            vysledek = kalkulacka.divide(a, b)

        print("Výsledek:", vysledek)

# Spuštění programu
hlavni_program()



# Co ses naučil:

#Definovat třídu Calculator.

#Každá operace (add, subtract,...) je metoda objektu.

#Objekt kalkulacka je vytvořen z třídy a používán v hlavním programu.

#Přehlednější a lépe udržovatelný kód.

