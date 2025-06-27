def get_book_text(path_):
    with open(path_) as f:
        return f.read()

def word_counter(path_):
    return len(get_book_text(path_).split())

def iterate_characters(book_string):
    letter_dictionary= {}
    for i in range(97,123):
        letter_dictionary[chr(i)]=0

    for letter in letter_dictionary:
        letter_dictionary[letter] = book_string.count(letter)
    
    return letter_dictionary.sort()
    #print(letter_dictionary)