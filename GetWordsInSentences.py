'''
The goal here is to find all unique words in a string sentance. 
Exclude all non-alphabet characters before and after a word
(but not in the middle). Return a dict with each unique word
and their frequency.
'''


def find_unique_words(sentence: str):
    unique_list_of_words = list(sentence)
    non_alphabet_chars = "!@#$%^&*()-_{}[]|\/`~<>,.?"


def test_sentence1():
    sentence = "This is a test sentence to test the function."

    assert find_unique_words(sentence) == {
        "this": 1,
        "is": 1,
        "a": 1, 
        "test": 2,
        "sentence": 1, 
        "to": 1, 
        "the": 1, 
        "function": 1
    }

def test_sentence2():
    sentence = "One is one, only one."

    assert find_unique_words(sentence) == {
        "one": 3,
        "is": 1, 
        "only": 1
    }

def test_sentence3():
    sentence = "Thirty-three is _33 which is three times eleven!!"

    assert find_unique_words(sentence) = {
        "thirty-three": 1, 
        "is": 2, 
        "which": 1, 
        "three": 1, 
        "times": 1, 
        "eleven": 1
    }