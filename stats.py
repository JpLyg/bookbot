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
    
    return letter_dictionary
    #print(letter_dictionary)

def sort_setup(e):
    return e["count"]

def list_of_dictionary(book_path):
    book = get_book_text(book_path)
    raw_dictionary = iterate_characters(book.lower()) 
    new_list = []
    for entry in raw_dictionary:
        new_list.append({"character":entry, "count":raw_dictionary[entry]})

    return new_list
#    new_list.sort(reverse=True,key=sort_setup)


