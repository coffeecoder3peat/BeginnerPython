prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quite' when you are finished.)"
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
