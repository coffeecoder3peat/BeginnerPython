class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in respnse to a command."""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """Simulate rolloing over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Skooch', 3)
my_second_dog = Dog('Tucker', 1)
my_dog.sit()
my_dog.roll_over()