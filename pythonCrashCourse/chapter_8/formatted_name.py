def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a fll name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name(first_name='philip', middle_name='chase', last_name='wilson')
print(musician)