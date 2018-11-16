from utils import DoublyLinkedList

class AnimalShelter:

    def __init__(self):
        self.dogs = DoublyLinkedList()
        self.cats = DoublyLinkedList()
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if animal.__class__ == Dog:
            self.dogs.append_left(animal)
        else:
            self.cats.append_left(animal)

    def dequeue_any(self):
        if self.dogs.length == 0:
            return self.dequeue_cat()
        elif self.cats.length == 0:
            return self.dequeue_dog()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.is_older_than(cat):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.pop()

    def dequeue_cat(self):
        return self.cats.pop()

class Animal:

    def __init__(self, name):
        self.name = name
        self.order = None

    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def is_older_than(self, animal):
        return self.order < animal.get_order()

    def __repr__(self):
        return self.name

class Cat(Animal): pass
class Dog(Animal): pass

shelter = AnimalShelter()
shelter.enqueue(Dog('Rex'))
shelter.enqueue(Cat('Garfield'))
shelter.enqueue(Cat('Tom'))
shelter.enqueue(Cat('Bob'))
shelter.enqueue(Dog('Benny'))
shelter.cats.display()
shelter.dogs.display()

while shelter.dogs.length != 0 or shelter.cats.length != 0:
    shelter.dequeue_any()

shelter.enqueue(Dog('Gatsby'))
shelter.dogs.display()
