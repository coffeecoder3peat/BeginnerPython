responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the persons name and response
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in a dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person repond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results.
print("\n--- Polling Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")