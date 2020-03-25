# Calculate the length of each word in the tuple:
# eg:1
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))

# eg2:
x = chr(97)
print(x)

print(list(''.join(map(chr,range(97,123)))))
print(list(map(chr, range(97, 123))))
print(list(map(chr, range(65, 91))))

