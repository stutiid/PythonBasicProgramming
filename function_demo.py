def checkPalindrome(num):
    """
    Checks whether the given number is palindrome or not and print the result accordingly
    :param num: the number to be checked if its palindrome or not
    """
    number = num
    reverse = 0
    while number != 0:
        rem = number % 10
        reverse = reverse * 10 + rem
        number = number // 10
    else:
        if num == reverse:
            print("number is palindrome")
        else:
            print("number is not palindrome")


def var_args_param(*numbers, **contactbook):
    """
    Demonstrate the use of variable arguments in the function argument list so if * is used with argument name then
    arguments will be taken as tuple and ** is used with argument name then it will be taken as dictionary
    :param numbers: as tuple with variable length
    :param contactbook: as dictionary argument with variable length
    """
    print("Variable arguments demo")
    print("tuple length", len(numbers))
    print("dictionary length", len(contactbook))
    for items in numbers:
        print("item:", items)
    for (key, value) in contactbook.items():
        print("[key:", key, ", value:", value, "]")


def empty_function():
    """
    Empty function creation is demonstrated using pass keyword as pass acts a placeholder for future code so when used
    inside empty function it avoids the error that came due to the use of empty function
    """
    pass


def maximum_number(num1, num2):
    """
    Demonstrate the usage of return statement. It determines the maximum number among the given two numbers
    :param num1: first number given by user
    :param num2: second number given by user
    :return : return the maximum number among the given two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2


def print_max(num1, num2):
    """
    Print the maximum of two numbers and numbers are to be integers only
    :param num1: first number given by user
    :param num2: second number given by user
    """
    num1 = int(num1)
    num2 = int(num2)

    if num1 > num2:
        print(num1, 'is maximum')
    else:
        print(num2, 'is maximum')


"""
File demonstrates the functions in python 
"""
checkPalindrome(int(input("enter number to check palindrome")))
var_args_param([1, 23, 4], Jack=123, John=133)
var_args_param(1, 23, 4, Jack=123, John=133)
print("empty function executing without error with pass", empty_function())
print("maximum number is", maximum_number(30, 45))
print_max(3, 5)
print(print_max.__doc__)
