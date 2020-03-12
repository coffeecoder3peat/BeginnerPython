digits = list(range(1,10))

for number in digits:
    if number == 1:
        ordinal_number = '1st'
    elif number == 2:
        ordinal_number = '2nd'
    elif number == 3:
        ordinal_number = '3rd'
    else:
        ordinal_number = f"{number}th"

    print(ordinal_number)