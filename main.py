def get_book_text(path_):
    with open(path_) as f:
        return f.read()

def word_counter(path_):
    return len(get_book_text(path_).split())
    #return "test"

def main():
    frankenstein_book_path = "books/frankenstein.txt"
    print(word_counter(frankenstein_book_path), "words found in the document")


    
#    print(get_book_text("books/frankenstein.txt"))
 
main()

