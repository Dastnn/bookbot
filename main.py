import sys
from stats import total_words, letters_total, word_list

def the_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(the_book):
    with open(the_book) as file:
        return file.read()

def main():
    book = the_book()
    print(
        "============ BOOKBOT ============\n"

        f"Analyzing book found at {book}...\n"

        "----------- Word Count ----------\n"

        f"Found {total_words(get_book_text)} total words\n"

        "--------- Character Count -------\n"

        f"{word_list(letters_total(get_book_text))}\n"

        "============= END ==============="
        )

main()