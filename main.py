from stats import count_words
from stats import count_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f'Found {num_words} total words')
    char_dict = count_characters(text)
    print(char_dict)


if __name__ == "__main__":
    main()
