class Restaurant:
    """Simple description of a restauraunt."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes"""

        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def show_restaurant_info(self):
        """Prints the restuarants information."""

        print(f"Name: {self.name}")
        print(f"Cuisine: {self.cuisine_type}")
        print(f"Customers Served: {self.number_served}")
    
    def set_number_served(self, number_served):
        """Sets the amount of people the restaurant has served."""
        self.number_served = number_served
    
    def increment_number_served(self, new_customers_served):
        """Increment the number of patrons served."""

        self.number_served += new_customers_served

class IceCreamStand(Restaurant):
    """Creates a child class of restaurant for an Ice Cream stand"""

    def __init__(self, name, cuisine_type= 'Ice Cream'):
        super().__init__(name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    
    def show_restaurant_info(self):
        """Prints the Ice Cream Stand information."""
        print(f"Name: {self.name}")
        print(f"Cuisine: {self.cuisine_type}")
        print(f"Customers Served: {self.number_served}")
        print("Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

chases_ice_cream = IceCreamStand("Chase's Ice Cream")
chases_ice_cream.show_restaurant_info()