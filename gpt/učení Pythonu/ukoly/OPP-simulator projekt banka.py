

class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  # Zapouzdřená proměnná

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Vloženo {amount} Kč")
        else:
            print("Částka musí být kladná.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Vybráno {amount} Kč")
        else:
            print("Nedostatek prostředků.")

    def get_balance(self):
        return self.__balance

# Ukázka použití
ucet = BankAccount("Petr")
ucet.deposit(1000)
ucet.withdraw(200)
print("Zůstatek:", ucet.get_balance())




#BankAccount
#-Tímto vytváříme třídu s názvem BankAccount.
#-Třída je šablona pro objekt, např. bankovní účet.


#def __init__(self, owner):
  #  self.owner = owner
#    self.__balance = 0
#Co to je:
#__init__() je konstruktor – spustí se automaticky při vytvoření objektu.

#-owner je vstupní parametr (např. jméno vlastníka účtu).
#-self.owner = owner uloží jméno vlastníka do objektu.
#-self.__balance = 0 vytvoří soukromou proměnnou (s dvěma podtržítky), aby k ní nešlo přistupovat přímo zvenčí (ucet.__balance by selhalo).
#- Zapouzdření (encapsulation) = schováváme vnitřní stav → bezpečnější a čistší.


#def deposit(self, amount):
   # if amount > 0:
  #      self.__balance += amount
   #     print(f"Vloženo {amount} Kč")
 #   else:
   #     print("Částka musí být kladná.")

#Co to je:
#Metoda deposit() přidá peníze na účet.
#Ověřuje, že částka je kladná.
#Mění __balance pomocí +=.


#def withdraw(self, amount):
#    if amount <= self.__balance:
  #      self.__balance -= amount
 #       print(f"Vybráno {amount} Kč")
 #   else:
 #       print("Nedostatek prostředků.")

#Co to je:
#Metoda withdraw() odečte peníze, ale jen pokud je dostatek.
#Ochrání nás před záporným zůstatkem.


#def get_balance(self):
 #   return self.__balance

#Co to je:
#Vrací zůstatek na účtu.
#Je to tzv. getter metoda – přístup k hodnotě bez její přímé manipulace.


#ucet = BankAccount("Petr")

#ucet.deposit(1000)
#ucet.withdraw(200)
#print("Zůstatek:", ucet.get_balance())


 




