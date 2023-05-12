class Animal():
    def __init__(self, name, species, age, gender):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
    
    def describe(self):
        print(f"{self.name} is a {self.age} year old {self.gender} {self.species}.")
    
    def feed(self, feed):
        print(f"{self.name} is eating {feed}.")

    def make_sound(self, sound):
        print(f"{self.name} is making a {sound} sound.")

    def move(self):
        print(f"{self.name} is moving.")

murphy = Animal("Murphy", "dog", "2", "boy")
murphy.describe()
murphy.make_sound("grrrrr")
murphy.feed("treats")

class Mammal(Animal):
    def __init__(self, name, species, age, gender, fur_color):
        super().__init__(name, species, age, gender)
        self.fur_color = fur_color

    def describe(self):
        print(f"{self.name} is a {self.fur_color} {self.age} year old {self.gender} {self.species}.")
    
    def feed(self, feed):
        return super().feed(feed)
    
    def make_sound(self, sound):
        return super().make_sound(sound)
    
    def move(self):
        return super().move()
    

henry = Mammal("Henry", "cat", "five", "boy", "white")
henry.feed("milk")
henry.make_sound("ppppppprrrrrr")
henry.move()
henry.describe()

class Zoo():
    def __init__(self, animals=[]):
        self.animals = animals
    
    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def display_animals(self):
        for animal in self.animals:
            animal.describe()

    def feed_animals(self):
        for animal in self.animals:
            animal.feed("food")

    def listen_to_animals(self):
        for animal in self.animals:
            animal.make_sound("bark bark bark")

    def watch_animals(self):
        for animal in self.animals:
            animal.move()



zoo = Zoo()

zoo.add_animal(henry)
zoo.add_animal(murphy)

zoo.display_animals()
zoo.feed_animals()
zoo.listen_to_animals()
zoo.watch_animals()



class Bird(Zoo):
    def __init__(self, animals=[], wingspan):
        super().__init__(animals)
    
    def add_animal(self, new_animal):
        return super().add_animal(new_animal)
    
    def feed_animals(self):
        return super().feed_animals()
    