favorite_languages = {
    'jen': 'python',
    'chase': 'python',
    'sarah': 'c',
    'edward': 'ruby'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.'")

# You can loop through keys of a dictionary using the keys() method.
# using no method is the same action as using keys() method
for name in favorite_languages.keys():
    print(name.title())

# You can also loop through the values of a dictionary using the values() method
for language in favorite_languages.values():
    print(language.title())

# You can use the set() function to only get unique items
for language in set(favorite_languages.values()):
    print(language.title())

# NOTE You can also create a set by using braces and separating values by commas

