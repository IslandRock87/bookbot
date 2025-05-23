from stats import word_count
from stats import num_char

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        lower = str.lower(file_contents)
    return lower

def main():
    # Get text from file in small letters"
    path_to_file = "/home/oysk/arbeid/github/bookbot/books/frankenstein.txt"
    text = get_book_text(path_to_file)


    # Count words
    c = word_count(text)

    # Count characters
    d = num_char(text)

    # Sort characters

    print("Word count: ", c)
    print(d)


main()

