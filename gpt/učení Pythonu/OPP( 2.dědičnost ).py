
class Animal:
    def speak(self):
        print("Nějaké zvíře vydává zvuk")

class Dog(Animal):
    def speak(self):
        print("Haf!")

class Cat(Animal):
    def speak(self):
        print("Mňau!")

zvire1 = Dog()
zvire2 = Cat()

zvire1.speak()  # Haf!
zvire2.speak()  # Mňau!

#Třída Dog a Cat dědí ze Animal a přepisují metodu speak
