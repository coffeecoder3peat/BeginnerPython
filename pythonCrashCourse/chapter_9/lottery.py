from random import choice

lottery_list = [
    '15',
    '8',
    '27',
    '90', 
    '77',
    '45',
    '99',
    '7',
    '35',
    '54',
    'a',
    'z',
    'g',
    's',
    'v'
]

my_ticket = []

for num in range(1,4):
    my_ticket += choice(lottery_list)

print(f"Your lottery ticket combination is: {my_ticket}")
count = 0
lottery_picks = ''
while my_ticket != lottery_picks:
    lottery_picks = []
    for num in range(1,4):
        lottery_picks += choice(lottery_list)
    count += 1

print(f"It only took you {count} rounds to win. Congratulations!")