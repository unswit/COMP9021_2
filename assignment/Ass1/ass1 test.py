Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Please convert XXXVI using XABVI
SyntaxError: invalid syntax
>>> from collections import Counter

try:
    name_of_file = input("How can I help you? ")
except ValueError:
    print("I don't get what you want, sorry mate!")
    sys.exit()
input_list = name_of_file.split(" ")
c = input_list[2]
print(list(c))
b = list(c)
count = Counter(b)
print(count)
SyntaxError: multiple statements found while compiling a single statement
>>> from collections import Counter

try:
    name_of_file = input("How can I help you? ")
except ValueError:
    print("I don't get what you want, sorry mate!")
    sys.exit()
input_list = name_of_file.split(" ")
c = input_list[2]
print(list(c))
b = list(c)
count = Counter(b)
print(count)
