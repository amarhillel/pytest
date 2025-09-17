class Zoo:
    def __init__(self):
        self._animals = []  # הכמסה – אוסף פרטי

    def add_animal(self, animal):
        self._animals.append(animal)

    def show_all(self):
        for a in self._animals:
            print(f"{a.info()} says {a.speak()}" )
