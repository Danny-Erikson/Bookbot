# Functions for analyzing books

def count_words(data):
    # Split words by spaces
    words = data.split()
    return len(words)


def count_characters(data):
    # Used to count the number of characters in a text
    char_count = {}
    for i in data:
        i = i.lower()
        # *If the character is already in the dictionary, add one to its count
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


def sort_on(items):
    # Helper function for filter
    return items["num"]


def filter(data):
    # Used to filter out non-alphabetical characters and create a dictionary of values sorted by frequency
    final = []
    for i in data:
        if i.isalpha():
            final.append({"char": i, "num": data[i]})
    final.sort(reverse=True, key=sort_on)
    return final
