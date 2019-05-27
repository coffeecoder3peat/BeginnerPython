file_path = 'pythonCrashCourse\chapter_10\programming.txt'

with open(file_path, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(file_path, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps tha can run in a browser.\n")