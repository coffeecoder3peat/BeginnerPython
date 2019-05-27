class Restaurant:
    """An example restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restuarant name and cuisine type."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"This restuarant's name is {self.name}.")
        print(f"This restaurant serves {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open.")

test_restaurant = Restaurant("Phil's", 'BBQ')

test_restaurant.describe_restaurant()
test_restaurant.open_restaurant()