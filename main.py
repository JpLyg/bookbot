from stats import *
from lessons import *
import sys

def main():
    #sys.argv.append('books/frankenstein.txt')
    #sys.argv.append(input("Enter Book Path: "))

    if len(sys.argv) <=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        print_report(sys.argv[1])
    except FileNotFoundError:
        print ("invalid directory")

    
    exit()
main()
 
