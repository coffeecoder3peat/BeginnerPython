cars = [
    'bmw',
    'audi',
    'toyota',
    'subaru'
]
print(cars)

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = [
    'bmw',
    'audi',
    'toyota',
    'subaru'
]
print("Here is the original list of cars:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

count = len(cars)
print(count)