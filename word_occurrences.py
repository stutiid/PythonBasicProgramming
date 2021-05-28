word_frequency = {}


def count_same_words(string):
    """
    It counts the number of occurrences of words in a sentence and store them in the word_frequency dictionary and then
    finally prints the dictionary
    :param string: sentence given by user from which words occurrences is to be counted
    """
    words_tuple = string.split(" ")  # split() returns a list
    for i in words_tuple:
        word_frequency.update({i: (word_frequency.get(i) or 0) + 1})
    else:
        print(words_tuple)
        print(word_frequency)


count_same_words(input("enter a sentence"))
