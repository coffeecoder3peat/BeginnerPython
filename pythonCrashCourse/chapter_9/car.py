class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set thed odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Print a statement saying the gas tank has been filled."""
        print("The gas tank has been filled.")

class Battery:
    """A simple attempt to odel a battery  for an elevtric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery_size(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} on a full charge.")
    

class ElectricCar(Car):
    """
    Represents aspects of a car, specific to electric vehicles.
    Then initialize attributes specific to an electric car.
    """
    def __init__(self, make, model, year):
        """Initialize arrributes of the parent"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Print a statement saying this car doen't have a gas tank."""
        print("This car doesn't have a gas tank.")

