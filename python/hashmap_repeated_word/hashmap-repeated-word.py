
from python.hashtable import hashtable

hashtable = hashtable()

def first_repeated_word(str):
    new_str = str.lower()
    # string = new_str

    for word in new_str:
        if hashtable.contains(word):
            return word