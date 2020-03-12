current_users = ['philip', 'chase', 'gabrielle', 'wilson', 'ruth']
new_users = ['michael', 'ryan', 'wilson', 'kaitlin', 'chase']

for user in new_users:
    if user in  current_users:
        print("That name is currently in use. Please enter another name.")
    else:
        print("That username is available.")