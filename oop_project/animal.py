from abc import ABC, abstractmethod

class Animal(ABC):  # מחלקה אבסטרקטית (אי אפשר ליצור ממנה אובייקט ישיר)
    def __init__(self, name, age):
        self._name = name       # שדה מוגן (encapsulation)
        self._age = age         # שדה מוגן (encapsulation)

    @abstractmethod
    def speak(self):
        """כל חיה חייבת לממש פונקציה זו"""
        pass

    def info(self):
        """פונקציה משותפת לכל החיות"""
        return f"{self._name}, age {self._age}"
