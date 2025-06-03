


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  # "__" = soukromá proměnná

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Nedostatek prostředků.")

    def get_balance(self):
        return self.__balance

# Použití
ucet = BankAccount("Petr")
ucet.deposit(1000)
ucet.withdraw(300)
print("Zůstatek:", ucet.get_balance())

#Nejde přistoupit přímo na __balance, jen přes metody.


