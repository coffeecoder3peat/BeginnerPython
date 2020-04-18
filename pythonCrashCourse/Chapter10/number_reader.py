import json

filename = 'Chapter10/Output/numbers.json'
with open(filename, 'r') as f:
    numbers = json.load(f)

print(numbers)