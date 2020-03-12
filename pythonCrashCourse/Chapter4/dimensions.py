# This is a tuple. Unlike lists, tuples are immutable.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This will highlight that you can't change a tuple value once created
# dimensions[0] = 100
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Whle you can't modify values in a tuple, you can redefine the entire tuple
dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
