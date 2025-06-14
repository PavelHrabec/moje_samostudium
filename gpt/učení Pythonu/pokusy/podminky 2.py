


procenta = int(input("Zadej výsledek testu v %: "))

if 90 <= procenta <= 100:
    print("Tvoje známka je: 1")
elif 75 <= procenta <= 89:
    print("Tvoje známka je: 2")
elif 60 <= procenta <= 74:
    print("Tvoje známka je: 3")
elif 45 <= procenta <= 59:
    print("Tvoje známka je: 4")
elif 0 <= procenta <= 44:
    print("Tvoje známka je: 5")
else:
    print("Špatně zadané procento – zadej číslo mezi 0 a 100.")


