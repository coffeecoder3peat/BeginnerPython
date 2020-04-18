def count_words(filename, search_word=''):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file.
        if search_word:
            words = contents.lower().split(search_word)
            num_words = len(words)
            print(f"The file {filename} has the word, '{search_word.strip()}' about '{num_words}' times.")
        else:
            words = contents.split()
            num_words = len(words)
            print(f"The file {filename} has about {num_words} words.")

filenames = ['Chapter10/Texts/alice.txt', '/Texts/little_women.txt', 'Chapter10/Texts/moby_dick.txt', 'Chapter10/Texts/siddhartha.txt']

for file in filenames:
    count_words(file, 'the ')