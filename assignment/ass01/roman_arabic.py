# Written by *** for COMP9021
import re
from collections import OrderedDict, Counter

# convert numbers to dict
def convert_letters_to_number_dict(inputs):
    # convert letter sequence to number sequence
    if inputs and len(set(inputs)) != len(inputs):
        return None
    inputs = inputs[::-1]
    letters = []
    for index in range(0, len(inputs), 2):
        first_value = int(10 ** (index / 2))
        letters.append((inputs[index], first_value))
        # check 是不是4，5的位置
        if index + 1 < len(inputs):
            second_value = int(5 * 10 ** (index / 2))
            letters.append((inputs[index:index + 2], second_value - first_value))
            letters.append((inputs[index + 1], second_value))
        # check是不是存在9的位置
        if index + 2 < len(inputs):
            third_value = int(10 ** ((index + 2) / 2))
            letters.append((inputs[index] + inputs[index + 2], third_value - first_value))

    # sort dictionary in reversed order
    letter_dicts = OrderedDict(reversed(letters))
    return letter_dicts


def roman_to_arabic(inputs, dicts=None):
    '''
    convert roman number to arabic number
    '''
    result = 0
    for i in range(len(inputs)):
        if inputs[i] not in dicts.keys():
            return None
        else:
            num = int(dicts[inputs[i]])
            # check if next place is larger than the current place, if so, the value should be deducted.
            if i + 1 < len(inputs) and dicts[inputs[i + 1]] > num:
                result -= num
            else:
                result += num
    # validate if it is right
    if arabic_to_roman(result, dicts) == inputs:
        return result
    else:
        return None


def arabic_to_roman(initial_arabic_number, dicts):
    result = []
    for rom, num in dicts.items():
        while initial_arabic_number >= num:
            initial_arabic_number -= num
            result.append(rom)
    return ''.join(result)


def convert_second(params):
    if params[3] != "using":
        print("Hey, ask me something that's not impossible to do!")
    else:
        roman_dicts = convert_letters_to_number_dict(params[4])
        if roman_dicts:
            if re.match(r'^([1-9]|[1-9][0-9]+)$', params[2]):
                result = arabic_to_roman(int(params[2]), roman_dicts)
            else:
                result = roman_to_arabic(params[2], roman_dicts)
            if result:
                print(f"Sure! It is {result}")
            else:
                print("Hey, ask me something that's not impossible to do!")
        else:
            print("Hey, ask me something that's not impossible to do!")


def get_next_value(letter_result, type=True):
    result = 1
    if letter_result:
        temp = max(letter_result.values())
        if type:
            if str(temp).startswith("1"):
                result = 5 * temp
            else:
                result = 2 * temp
        else:
            if str(temp).startswith("5"):
                result = temp * 2
            else:
                result = temp * 10

    return result


def convert_third(params):
    if params[3] != "minimally":
        print("I don't get what you want, sorry mate!")
    elif re.match(r'\d', params[2]):
        print("Hey, ask me something that's not impossible to do!")


def convert_first(params):
    input_param = params[2]
    dicts = convert_letters_to_number_dict("MDCLXVI")
    if re.match(r'^([1-9]|[1-3][0-9]{1,3})$', input_param):
        result = arabic_to_roman(int(input_param), dicts)
    else:
        result = roman_to_arabic(input_param,dicts)

    if result:
        print(f"Sure! It is {result}")
    else:
        print(f"Hey, ask me something that's not impossible to do!")


def please_convert():
    params = input('How can I help you? ').split(" ")
    # params = "Please convert ABCADDEFGF minimally".split(" ")
    if 3 <= len(params) <= 5 and \
            params[0] == "Please" and params[1] == "convert":
        if len(params) == 3:
            convert_first(params)
        elif len(params) == 5:
            convert_second(params)
        else:
            convert_third(params)
    else:
        print("I don't get what you want, sorry mate!")


# DEFINE OTHER FUNCTIONS

please_convert()
# print(convert_letters_to_number_dict())
