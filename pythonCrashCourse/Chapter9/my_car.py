from car import Car
from random import randint

print(randint(1, 10))

my_new_car = Car('Toyota', 'Highlander', 2015)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()