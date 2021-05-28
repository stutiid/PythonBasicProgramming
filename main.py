"""
File demonstrate the different data types in python
"""
# String data type
num1 = input('enter first number:')
num2 = input('enter second number:')
print('The addition of a and b is:', (num1 + num2))
num1 = int(input('enter  first number:'))
num2 = int(input('enter second number:'))
print('The addition of two number is:', (num1 + num2))

# numeric data types
num1 = 10
num2 = -10
num3 = 3.142
num4 = 0.142
num5 = 10 + 3j
num6 = 6j
print(num1 + num2, num3 - num4, num5 - num6, end='\n')
print(num1 - num3, num2 - num6, num1 * num2, end='\n')
print(3 ** 4)  # to print power
print(-13 // 5, "", 9 // 1.81)
# convert decimal to hex and octal
print("convert number in hex " + hex(56))
print("convert number in oct " + oct(56))
# convert string in binary to int
s = "10010"
num3 = int(s, 2)
print("String in binary to int : ", num3)

# complex data type
print("Complex data type : ", 3 + 5j + 4 + 6j)

# list data types
my_list = []
print(my_list)
my_list_2 = list()
print(my_list_2)
my_list = [1, 2, 3, 'edureka', 'python']
my_list_2 = list([4, 5, 3.14, 'fun', 4.55])
print(my_list)
print(my_list_2)
# print element in reverse order
print(my_list[::-1], end='\n')
# to print only last element and second last element
print(my_list_2[-1], " " + my_list_2[-2])
# accessing all elements at a go
print(my_list[:])  # or print(my_list)
# access elements between a range exclusive of higher bound
print(my_list_2[1:4])
# use of skipping index
print(my_list[0:4:3])
# add elements to the list using insert, append and extend. append  add as a single element
my_list.append([555, 'you'])
print(my_list)
print(len(my_list))
# extending list by adding all the elements one by one
my_list_2.extend([555, 12])
print(my_list_2)
print(len(my_list_2))
# insert will add elements  at a specific index and don't delete the element already present there its just pushes the
# data one step ahead to make room for the new element
my_list.insert(1, "insert example")
print(my_list)
print(len(my_list))
# deleting elements from list
del my_list[6][0]
print(my_list)
my_list_2.remove(555)
print(my_list_2)
num1 = my_list.pop(1)
print('Popped Element: ', num1, 'List remaining ', my_list)
print(my_list.index('edureka'))
print(my_list.count('edureka'))
# for using sort the data types of the elements must be same
new = [5, 4, 12, 45, 3]
print(sorted(new))  # sorts the elements in the list but does not change the original
print(new)
# sorts the original list in descending order if reverse=True and if no reverse is given it will sort in ascending order
new.sort(reverse=True)
print(new)
new.reverse()  # reverses the list elements
print(new)

# tuple data type
my_tuple = ()
my_tuple_2 = tuple()
my_tuple = (1, 2, 3)
my_tuple_2 = tuple(('Python', 'for', 'edureka'))
# to have a single element in the tuple use , at the end
my_tuple_3 = ('example',)
print(my_tuple)
print(len(my_tuple))
print(my_tuple_2)
print(len(my_tuple_2))
print(my_tuple_3)
print(len(my_tuple_3))

# dictionary data type
address_book = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", address_book['Swaroop'])
# Deleting a key-value pair
del address_book['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(address_book)))
for name, address in address_book.items():
    print('Contact {} at {}'.format(name, address))
address_book['Guido'] = 'guido@python.org'
if 'Guido' in address_book:
    print("\nGuido's address is", address_book['Guido'])
address_book.pop('Swaroop')

# sets data type
countries = set(['brazil', 'russia', 'india'])
if 'india' in countries:
    print(True)
countries_list = countries.copy()
countries_list.add('china')
if countries_list.issuperset(countries):
    print(True)
countries.remove('russia')
print(countries & countries_list)  # or bri.intersection(bric)
