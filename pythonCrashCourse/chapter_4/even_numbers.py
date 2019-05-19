even_numbers = list(range(2, 11, 2))
print(even_numbers)

#for value in range(1, 21):
    #print(value)
digits = range(1, 1000000000)
#for value in digits:
    #print (value)

#odd_numbers = range(1,21,2)
#for value in odd_numbers:
#    print(value)
#threes = range(0, 31, 3)
#for value in threes:
#    print(value)

#cubes = []
#for value in range(1, 11):
#    cube = value ** 3
#    cubes.append(cube)
#
#print(cubes)

cubes = [value ** 3 for value in range(1,21)]
print(cubes)