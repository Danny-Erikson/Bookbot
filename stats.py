def count_words(data):
    words = data.split()
    return len(words)


def count_characters(data):
    char_count = {}
    for i in data:
        i = i.lower()
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
