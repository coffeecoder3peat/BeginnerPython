def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

formatted_name = build_person('chase', 'wilson', 27)
print(formatted_name)