
def word_count(text):
    words = text.split()
    n = 0
    for word in words:
        n +=1
    return n

def num_char(book):
    char = list(book)

    letters = {}

    for letter in char:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters

def sort_characters(letters):
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    return sorted_letters
    
