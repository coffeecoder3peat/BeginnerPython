users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'prinston'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"

    print(f"\tFull Name: {full_name}")
    print(f"\tLocation: {user_info['location'].title()}")