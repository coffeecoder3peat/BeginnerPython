# Start with the users that need to be verified,
# and an empyt list to hold confirmed users.
unconfirmed_users = ['alica', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("The following users have been confirmed:")
for user in confirmed_users:
    print(user.title())