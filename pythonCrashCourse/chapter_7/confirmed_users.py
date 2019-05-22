# Start with useers that need to be verified and an empty
# list to hold confirmed users.
unconfimred_users = [
    'alice',
    'brian',
    'candace'
]

confirmed_users = []

# Veerify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfimred_users:
    current_user = unconfimred_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all current users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())