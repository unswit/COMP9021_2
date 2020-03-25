#if 只会输出为true的值
# eg:1
is_male = True

if is_male:
    print("You are a male")

# eg:2
is_adult = False

if is_adult:
    print("You are an adult")#print nothing, because is_adult is Falese
else:
    print("You are not an adult")

# eg:3
is_child = True

if is_child:
    print("You are a child")
else:
    print("You are not a child")

#eg:4
is_femal = True
is_tall = True

if is_tall or is_femal:
    print("You are a tall or a female or both")
else:
    print("You neither female nor tall")

#eg:5
is_femal = False
is_tall = True

if is_tall or is_femal:
    print("You are a tall or a female or both")
else:
    print("You neither female nor both")

#eg:6
is_femal = False
is_tall = True

if is_tall and is_femal:
    print("You are a tall female or both")
else:
    print("You neither female nor tall")

#eg:7
is_femal = False
is_tall = False

if is_tall and is_femal:
    print("You are a tall female")
else:
    print("You neither female nor tall or not tall or both ")

#eg:7
is_femal = True
is_tall = False

if is_tall or is_femal:
    print("You are a tall or a female or both")
else:
    print("You neither female")

#eg:8  what is I want to check femal not tall
is_female = True
is_tall = False

if is_tall and is_female:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_male) and is_tall:
    print("You are a female but you are tall")
else:
    print("You are not female and not tall")

# eg9:
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")