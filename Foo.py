class Foo(): # creating a class Foo
    def __init__(self,name,profession): #intiializer method 
        self.name=name
        self.profession=profession        
    def __repr__(self):
        return f"Foo({self.name}, {self.profession})" #added a space here
    def speak(self):
        return f"{self.name} says hello!"
