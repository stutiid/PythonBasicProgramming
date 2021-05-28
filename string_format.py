"""
File demonstrate the usage of format function in string and raw string
"""
name = "Stuti"
languageName = 'Python'
print('Hello {} welcome to {}'.format(name, languageName))
print('Hello {name} welcome to {language}'.format(name=name, language=languageName))
print(f'Hello {name}')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0 / 3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0}{1:_^14}'.format('hello', 'there'))

print('a', end='')
print('b', end='')
print(end='\n')

s = r"Newlines are indicated by \n and to escape ', :, or any other symbol with already defined meaning use row string "
print(s)
