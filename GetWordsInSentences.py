'''
The goal here is to find all unique words in a string sentance. 
Exclude all non-alphabet characters before and after a word
(but not in the middle). Return a dict with each unique word
and their frequency.
''' 

non_alphabet_chars = "!@#$%^&*()-_{}[]|\\/`~<>,.?"
non_alphabet_chars_list = list(non_alphabet_chars)

def trim_string(string_word):
    """ Recursive solution for removing non-alphanumberic characters from ends of string."""

    # base cases
    if len(string_word) == 0:
        return string_word

    elif (string_word[0] not in non_alphabet_chars_list and
        string_word[-1] not in non_alphabet_chars_list):
        return string_word

    elif string_word[0] in non_alphabet_chars_list:
        string_word = string_word[1:]
        return trim_string(string_word)
    
    elif string_word[-1] in non_alphabet_chars_list:
        string_word = string_word[:-1]
        return trim_string(string_word)

def find_unique_words(sentence: str):
    """ Function for finding unique words in string sentence. Returns dict w/ word frequency."""

    unique_list_of_words = sentence.split()

    output_dict = {}
    for word in unique_list_of_words:
        lowercase_word = word.lower()
        no_chars_word = trim_string(lowercase_word)
        if len(no_chars_word) != 0:
            if no_chars_word in output_dict.keys():
                output_dict[no_chars_word] += 1
            else:
                output_dict[no_chars_word] = 1

    return output_dict


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

    assert find_unique_words(sentence) == {
        "thirty-three": 1, 
        "is": 2, 
        "33": 1,
        "which": 1, 
        "three": 1, 
        "times": 1, 
        "eleven": 1
    }


if __name__ == "__main__":
    test_sentence1()
    test_sentence2()
    test_sentence3()