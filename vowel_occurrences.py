frequency_map = {}


def count_frequency(string):
    """
    It counts the number of occurrences of vowels in a string and store them in the frequency_map dictionary and finally
    prints the dictionary
    :param string: string given by user from which vowels occurrences is to be counted
    """
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            frequency_map.update({char: (frequency_map.get(char) or 0) + 1})
        else:
            continue
    else:
        print(frequency_map)


def check_palindrome(string):
    """
    Print palindrome if given sentence is a palindrome else print not palindrome. By removing the delimiters sentence is
    converted into a string and then string is reversed and reversed string and original string is compared to check the
    palindrome
    :param string: sentence given by user to check if its palindrome or not
    """
    delimiters = (",", " ", ".", ":")
    for i in delimiters:
        if string.__contains__(i):
            string = string.replace(i, "")
    string = string.lower()
    reverse = string[::-1]
    if string == reverse:
        print("palindrome")
    else:
        print("not palindrome")


count_frequency(input("enter the string"))
check_palindrome("Rise to vote, sir.")
