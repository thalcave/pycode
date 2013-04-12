#!/usr/bin/env python

def word_count(text, case_sensitive=True):
    """counts the number of occurences in text"""

    # if not case sensitive
    if not case_sensitive:
        text = text.lower()

    # usage of split(" ") will not group together consecutive delimiters
    item_list = text.split()

    # keep words counter
    counter = {}

    for x in item_list:
        counter[x] = 1 + counter.get(x, 0)


    print counter

    return counter

def test_word_count():
    assert word_count("a b c") == dict(a=1, b=1, c=1)
    assert word_count("a b a") == dict(a=2, b=1)
    assert word_count("a b A") == dict(a=1, b=1, A=1)
    assert word_count("a b A", False) == dict(a=2, b=1)

            
    
if __name__ == '__main__':
    test_word_count()
