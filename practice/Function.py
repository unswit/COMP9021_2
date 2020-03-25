#def a function

#Return
def cube(num):
    return num*num*num#return is the end of the function,will go out this function.so
    print("result1:","code")#this line would not be print out
print(cube(2))
result=cube(2)# or store the number in result than print the result
print(result)

def sayhi():#def a function a name
    print("Hello User")

sayhi()


def say_hi(name,age):
    print("Hello "+name+"You are " + str(age))#we can't in put number untill add str(),otherwise we can only input "1" or "2"

say_hi("Mike",1)
say_hi("Steve",2)



temp = input("input a number:")
guess = int(temp)
if guess == 8:
    print("You are right")
else:
    print("You are wrong")



word = input("input:")
word.isalpha()
print(word)

