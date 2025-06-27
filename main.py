from stats import *

def main():
    target_book = "books/frankenstein.txt"
    print(word_counter(target_book),"words found in the document")
    print(iterate_characters(get_book_text(target_book).lower()))

main()

