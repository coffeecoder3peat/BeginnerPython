alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right
# Determin how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] = x_increment
print(f"New position: {alien_0['x_position']}")

print(alien_0)
del alien_0['points']
print(alien_0)