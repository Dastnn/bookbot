import sys

def total_words(get_book_text):
    text = get_book_text(sys.argv[1])
    words = text.split()
    return len(words)

def letters_total(get_book_text):
    text = get_book_text(sys.argv[1])
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def word_list(letters_total):
    sorted_dict = sorted(letters_total, key=letters_total.get, reverse=True)
    new_list = []
    pretty_string = ""
    for letter in sorted_dict:
        appended_string = f"{letter}: {letters_total[letter]}"
        new_list.append(appended_string)
    for string in new_list[-1::-1]:
        pretty_string = string + "\n" + pretty_string
    return pretty_string