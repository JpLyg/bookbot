def get_book_text(path_):
    with open(path_) as f:
        return f.read()

def word_counter(path_):
    return len(get_book_text(path_).split())