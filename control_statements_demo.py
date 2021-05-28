"""
File demonstrate the control statements in python like for loop, while and if elif ladder
"""
num = int(input("enter a number to check prime"))
flag = False
for i in range(2, num // 2): # same java foreach loop
    if (num % i) == 0:
        # flag = True
        print("number is not prime")
        break
else:
    print("number is prime")

# while loop demo
while flag:
    print("It is will not execute")
else:
    print("only else part will execute as condition is false now")

# if else ladder example
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
