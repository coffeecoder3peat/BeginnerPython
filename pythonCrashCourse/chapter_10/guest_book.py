file_path = 'pythonCrashCourse\chapter_10\guest.txt'

with open(file_path, 'a') as file_object:
    name = ''
    while name != 'done':
        name = input("Please enter your name in the guestbook. If you are the last person, please enter 'done': ")

        if name == 'done':
            break

        file_object.write(f"{name}\n")
