class InputError(Exception):
    # init
    def __init__(self, message = ''):
        self.message = message

class Ass01FirstError(Exception):
    def __init__(self, message = ''):
        self.message = message

class Ass02FirstError(Exception):
    def __init__(self, message = ''):
        self.message = message

def convert_extend_roman_to_dict(romans = "IVXLCDM"):
    result = {}
    start = 1
    if romans:
        for cur_index in range(0, len(romans), 2):
            cur_roman = romans[cur_index]
            result[cur_roman] = start

            if cur_index + 1 < len(romans):
                next_roman = romans[cur_index + 1]
                # IV
                result[cur_roman + next_roman] = 4 * start
                # v
                result[next_roman] = 5 * start

            if cur_index + 2 < len(romans):
                next_next_roman = romans[cur_index + 2]
                # IX
                result[cur_roman + next_next_roman] = 9 * start
                # X
                result[next_next_roman] = 10 * start

            start *= 10

    return result


def convert_standard_roman_to_dict(romans = "IVXLCDM"):
    result = {}
    start = 1
    if romans:
        first = romans[0]
        result[first] = start

        for next_item in romans[1:]:
            if str(start).startswith("1"):
                start = start * 5
            else:
                start = start * 2
            result[next_item] = start
    return result


def convert_roman_to_number(roman_input,roman_dict = None):
    # {I:1,IV:4,V:5}
    if roman_dict is None:
        roman_dict = convert_extend_roman_to_dict()
    result = None
    if roman_input:
        result = 0
        # VII
        index = 0
        while index < len(roman_input):
            cur_roman = roman_input[index]
            cur_roman_number = roman_dict[cur_roman]
            if index + 1 < len(roman_input):
                next_roman = roman_input[index + 1]
                next_roman_number = roman_dict[next_roman]
                if next_roman_number > cur_roman_number:
                    result += next_roman_number - cur_roman_number
                    index += 2
                    continue
            result += cur_roman_number
            index += 1
    else:
        raise InputError("")

    return result


def convert_number_to_roman(number,roman_dict = None):
    # {I:1,IV:4,V:5}
    if roman_dict is None:
        roman_dict = convert_extend_roman_to_dict()
    # {1:I,4:IV,5:V}
    number_roman_dict = {v: k for k, v in roman_dict.items()}

    # number = 7
    result = ""
    keys = number_roman_dict.keys()
    # 1000,900,500,400,100,90,50,40,10,9,5,4,1
    keys = sorted(keys, reverse=True)
    cur_number =int(number)
    for key in keys:
        while cur_number >= key:
            result += number_roman_dict.get(key)
            cur_number -= key

    return result

def check_second_input(params):
    test_roman = params[0]
    romans = params[2][::-1]
    roman_result = convert_standard_roman_to_dict(romans)

    if not romans.isalpha() or not test_roman.isalpha():
        raise InputError("")

    for k,v in roman_result.items():
        if str(v)[0] == '5' and test_roman.find(k * 2) > -1:
            raise InputError("")
    for item in test_roman:
        if item * 4 in test_roman:
            raise InputError("")
    for item in test_roman:
        if item * 4 in test_roman:
            raise InputError("")




try:

    user_input = input("Can I help you?")
    if user_input:
        if user_input.startswith("Please convert "):
            user_input = user_input.replace("Please convert ", "").strip()
            params = user_input.split(" ")
            if len(params) == 1:
                if params[0].isdigit():
                    if params[0].startswith("0"):
                        raise InputError("")
                    else:
                        number = int(params[0])
                        if number < 1 or number >= 4000:
                            raise InputError("")
                        else:
                            roman_result = convert_number_to_roman(number)
                            exp_result = convert_roman_to_number(roman_result)
                            if exp_result == number:
                                print(f"It's Sure {roman_result}")
                            else:
                                raise InputError("")
                else:
                    # for e in params[0]:
                    #    if e not in "IVXLCDM":
                    #         raise InputError("")
                    not_romans = [e for e in params[0] if e not in "IVXLCDM"]
                    if not_romans:
                        raise InputError("")
                    else:
                        for item in params[0]:
                            if item * 4 in params[0]:
                                raise InputError("")
                        # convert roman input to number
                        number = convert_roman_to_number(params[0])
                        exp_roman = convert_number_to_roman(number)
                        if params[0] == exp_roman:
                            print(f"It's Sure {number}")
                        else:
                            raise InputError("")
            elif len(params) == 3:
                if params[1] !="using":
                    raise InputError("")
                # check all the input
                check_second_input(params)
                roman_dict_convert = convert_extend_roman_to_dict(params[2][::-1])
                number = convert_roman_to_number(params[0],roman_dict_convert)
                exp_roman = convert_number_to_roman(number,roman_dict_convert)
                if params[0] == exp_roman:
                    print(f"It's Sure {number}")
                else:
                    raise InputError("")

            elif len(params) == 2:
                pass
            else:
                raise InputError("")
        else:
            raise InputError("")
    else:
        raise InputError("")
except InputError:
    print("Hey, ask me something that's not impossible to do!")
except TypeError:
    print("Sorry! M")
