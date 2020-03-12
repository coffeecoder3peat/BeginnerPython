players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# You can also omit the fist index and Python will know to start from 0
print(players[:3])

# Vice versa, you can opit the last index and Python will know to go until the last of the list
print(players[2:])

# Slicing will also allow you to use the differnt forms of indexing lik using negative to represent an amount from the last index
print(players[-3:])

# You can also add a third value to tell python how many values to skip
print(players[0:3:2])

# This shows how to loop through a lice of a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())