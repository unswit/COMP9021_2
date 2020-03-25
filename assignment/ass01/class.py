romans = "IVXLCM"

def convert_first_number(input):
    roman_format = "IVXLCM"
    result =  convert_first_roman_dict(roman_format)
    reversed_result = {value:key for key,value in result.items()}

    output = ""
    # keys = sorted( reversed_result.keys(),reverse=True)
    keys = reversed( sorted(reversed_result.keys()))
    number = int(input)
    for key in keys:
        while number >= key:
            number = number - key
            output += reversed_result.get(key)

    return output

def convert_first_roman(input):
    roman_format = "IVXLCM"
    # input = VIII
    result = convert_first_roman_dict(roman_format)
    index = 0
    output = None
    if input:
        output = 0
        while index < len(input):
            cur_roman = input[index]
            cur_roman_number = result.get(cur_roman)

            if index + 1 < len(input):
                next_roman = input[index + 1]
                next_roman_number = result.get(next_roman)
                if cur_roman_number < next_roman_number:
                    output += next_roman_number - cur_roman_number
                    index +=2

            output += cur_roman_number
            index += 1

    return output


def convert_first_roman_dict(input):
    result = {}
    if input:
        start = 1
        # IVXLCM
        # I
        # IV
        # AB
        # ABC
        # abcdefghijklmnxyzAZF
        for index in range(0,len(input),2):
            result[input[index]] = start
            if index + 1 < len(input):
                result[input[index] + input[index + 1]] = 4* start
                result[input[index + 1]] = 5* start
            if index + 2 < len(input):
                result[input[index] + input[index + 2]] = 9 * start
                result[input[index + 2]] = 10 * start
            start = 10 *start
        # reverse_result = {value:key for key,value in result.items()}
    return result

def convert_first_roman_1(input):
    # IVXLCM
    result = {}
    start = 1
    if input:
        result[input[0]] = start
        for index in range(len(input)):
            if index % 2 == 0:
                start *= 5
            else:
                start *=2
            result[input[index]] = start

        for item in input[1:]:
            if str(start)[0] == '1':
                start *=5
            else:
                start *=2
            result[item] = start
# I:1
# V:5:
# X:10


def check_first_convert(input = ""):
    if input.isdigit():
        if input.startswith("0"):
            return None
        elif 1<=int(input) <=3999:
            return convert_first_number(input)
        else:
            return None
    else:
        for item in input:
            if item not in romans:
                return None
        return convert_first_roman(input)

user_input = input("Can I help you? ")
if user_input:
    items = user_input.strip().split(" ")
    if user_input.startswith("Please convert ") and len(items) in (3,4,5):
        if len(items) == 3:
            print(check_first_convert(items[2]))
        elif len(items) == 4:
            # check_second_convert(items[2])
            pass
        else:
            # check_third_convert(items[2])
            pass
    else:
        print("Wrong")

else:
    print("Wrong")