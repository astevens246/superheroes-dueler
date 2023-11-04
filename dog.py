class Dog: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
  # Methods are defined as their own named functions inside the class
  # Remember to put the "self" parameter every time we make a class method!def bark(self):
    def bark(self):   
        print("Woof!")
# the same instantiation call that creates a Dog object,
# but now we've assigned it to the value of the my_dog variable

my_dog = Dog("Rex","Superdog")

