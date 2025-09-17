from dog import Dog
from cat import Cat
from zoo import Zoo

def main():
    # יוצרים חיות
    dog = Dog("Buddy", 3)
    cat = Cat("Misty", 2)

    # מפעילים פונקציות מיוחדות
    print(dog.fetch())
    print(cat.scratch())

    # יוצרים גן חיות
    zoo = Zoo()
    zoo.add_animal(dog)
    zoo.add_animal(cat)

    # מציגים את כל החיות → פולימורפיזם (כל חיה מדברת אחרת)
    zoo.show_all()

if __name__ == "__main__":
    main()
