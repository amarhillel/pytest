from animal import Animal

class Cat(Animal):  # ירושה
    def speak(self):  # פולימורפיזם (מימוש ייחודי ל-Cat)
        return "Meow!"

    def scratch(self):
        return f"{self._name} is scratching the furniture!"
