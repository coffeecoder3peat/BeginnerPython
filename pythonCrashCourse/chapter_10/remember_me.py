import json
def get_stored_user_profile():
    """Get stored username if available."""
    filename = 'user_profile.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user_profile():
    username = input("What is your name? ")
    favorite_color = input(f"What is your favorite color, {username}? ")
    user_profile = {
        'username' : username,
        'favorite_color' : favorite_color
    }

    print(f"We'll remember you next time, {username}.")
    filename = 'user_profile.json'
    with open(filename, 'w') as f:
        json.dump(user_profile, f)


def greet_user():
    """Greet user by name."""
    username = get_stored_user_profile()
    if username:
        verification = ''
        while verification != 'y' or verification != 'n':
            verification = input(f"Is your name {username['username']}? y/n: ")
            if verification == 'y':
                print(f"Welcome back, {username['username']}!")
                break
            elif verification == 'n':
                get_new_user_profile()
                break
            else:
                print(f"{verification} is not a valid answer. Please enter 'y' or 'n'.")
    else:
        get_new_user_profile()

greet_user()