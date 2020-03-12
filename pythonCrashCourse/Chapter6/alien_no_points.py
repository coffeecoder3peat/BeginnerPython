# If there is a chance the key you're asking for might not exist, 
# use the get() method to set a default value if no key is found

alien_0 = {
    'color': 'green',
    'speed': 'slow'
}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)