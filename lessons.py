from stats import *

def print_report(target_book): 
    #boot.dev Bookbot CH:3 L1 Print a report
    list_to_print = []

    character_count=list_of_dictionary(target_book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(target_book)} total words")
    print("--------- Character Count -------")

    list_to_print = list_of_dictionary(target_book)
    list_to_print.sort(reverse=True, key=sort_setup)

    for entry in list_to_print:
        print(f"{entry["character"]}: {entry["count"]}")
    