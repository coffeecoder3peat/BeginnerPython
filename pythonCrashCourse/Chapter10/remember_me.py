import json

def get_stored_username():
    """Get the username from json file."""
    filename = "Chapter10/output/username.json"
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Ask user what their username is."""
    username = input("What is your name? ")
    filename = "Chapter10/Output/username.json"

    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
