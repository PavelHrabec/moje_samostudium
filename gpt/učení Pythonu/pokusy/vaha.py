



váha = input("Kolik važíš?")
váha_kg = float(váha)
váha_g = váha_kg * 1000

print(f"Tolik {váha_kg} je tolik {váha_g} gramů.")

# Vysvětlení:
#input() → řetězec, např. "70"

#float(...) → převede na číslo: 70.0

#* 1000 → převede na 70000.0

#f-string → použije hodnoty uvnitř textu