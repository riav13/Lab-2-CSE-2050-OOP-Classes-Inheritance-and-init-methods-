class Animal:
    def __init__(self, name, species = "animal", sound = "hi"):
        """
        
        """
        self.name = name
        self.species = species
        self.sound = sound
    def __repr__(self):
        return f"Animal({self.name}, {self.species}, {self.sound})"
    def speak(self):
        return (f"{self.name}, a {self.species}, says {self.sound}!")
    

class Dog(Animal): #inhertiting traits from the animal class
    def __init__(self, name, species = "dog", sound = "ruff", is_good_boy = True):
        super().__init__(name, species, sound) #calls init method from parent class
        self.is_good_boy = is_good_boy
    def __repr__(self):
        return f"Dog({self.name})" #for dogs, its only supposed to return the name 
    #fstring , used to put variables into the string 

class Cat(Animal):
    def __repr__(self):
        return f"Cat({self.name}, {self.species}, {self.sound})"
    



