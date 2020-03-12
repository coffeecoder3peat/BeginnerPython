favorite_languages = {
    'jen': 'python',
    'chase': 'python',
    'sarah': 'c',
    'edward': 'ruby'
}

names_to_poll = ['jen', 'chase', 'john', 'edward', 'jack']

for name in names_to_poll:
    poll_status = favorite_languages.get(name)

    if poll_status:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, I see you haven't taken a poll yet. Please do so if you have the time.")

