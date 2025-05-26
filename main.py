from stats import word_count
from stats import num_char
from stats import sort_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        lower = str.lower(file_contents)
    return lower

def main():
    # Get text from file in small letters"
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1] 
        text = get_book_text(path_to_file) 

        # Count words

        c = word_count(text)

        # Count characters
        d = num_char(text)

        # Sort characters
        f = sort_characters(d)

        # Print results
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {c} total words")
        print("----------- Character Count ----------")
        for char, count in f:
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============") 
    
    
    


    


main()

