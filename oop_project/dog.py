from animal import Animal

class Dog(Animal):  # ירושה
    def speak(self):  # פולימורפיזם (מימוש ייחודי ל-Dog)
        return "Woof!"

    def fetch(self):
        return f"{self._name} is fetching the ball!"
