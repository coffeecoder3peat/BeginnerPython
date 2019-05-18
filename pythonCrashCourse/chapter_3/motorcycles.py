motorcycles = [
    "honda",
    "yamaha",
    "suzuki",
]

print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = [
    "honda",
    "yamaha",
    "suzuki",
]

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)