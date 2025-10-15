# Used to import a book to be analyzed
import sys

# Funtions for analyzing books, See stats.py for more details
from stats import count_words
from stats import count_characters
from stats import filter


def get_book_text(path):
    # Used to import a book to be analyzed
    with open(path) as f:
        return f.read()


def main():
    # Check for correct usage
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    # Start of the program
    print('============ BOOKBOT ============')
    text = get_book_text(sys.argv[1])
    print(f'Analyzing book found at {sys.argv[1]}')

    # Word Count
    num_words = count_words(text)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')

    # Character Count
    print('--------- Character Count -------')
    char_dict = count_characters(text)
    for i in filter(char_dict):  # *Loop through filtered characters
        print(f'{i['char']}: {i['num']}')
    print('============= END ===============')


# Runtime
if __name__ == "__main__":
    main()
