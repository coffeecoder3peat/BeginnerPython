alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

# You can also add key value pairs to the existing dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# You can start with an empty dictionary and add to it
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# You can modify the values of a dictionary
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Update the aliens location regularly
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine hwo far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# You can delete keys from a dictionary
print(alien_0)

del alien_0['points']
print(alien_0)
