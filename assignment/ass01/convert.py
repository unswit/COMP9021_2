from collections import OrderedDict

ARABIC_TO_ROMAN = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
])

ARABIC_TO_ROMAN = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
])

romams="I,IV,V,IX,X"
numbers = "1,4,5,9,10"


def get(cur):
    if cur is None:
        return 1
    else:
        if str(cur)[0] == '1':
            return cur * 5
        else:
            return cur * 2

line = "IVXLCDMOPQXYZabcdefghijklmn"
cur = None
roman_dic = {}
roman_dic = {
    "I":1,
    "V":5,
    "X":10,
    "L":50
}
for index in range(len(line)):
    roman_dic[line[index]] = get(cur)


# 1.如果出现了相连续的数字
#   a.不可能出现4个连续     IIII
#   b.如果是升序，不可能出现两个连续的   I 1 X 10   IIX  VIII
#   c.如果出现2个连续的，这两个连续的一定是10幂次方 10**0  10**1
#   d.DED 肯定是19 或者是19的 10**n的数字 19*10**n
# 如果从右向左开始计算，第一个和第三个相等，那么E是1*10**n D是1 * 10**（n+1）
#   e.ABCA 罗马数字表示的最小数字49 或者是49的 10**n的数字 49*10**n
#   190   CXC
#
#
#
# 2. (1 I  4 IV    9 IX,  49 XLIX)
# D 50 C 10 B 5 A 1     1 A    4 AB  9 AC    49 CDAC

# 1 5
# 10 50
# 100 500
# 1000 5000
# 10000 50000
#
# 1*10**0     1*10**1      1*10**2
# 1         5 10        50 100          500  1000
# I         V X         L  C            D    M
#
# 降序表示累加，升序表示累减
# 1     I
# 2     II
# 3     III
# 4     IV 1 5   5-1 4
# 5     V
# 6     VI 5 1    6
# 7     VII 5 1 1 7
# 8     VIII 5 1 1 1 8
# 9     IX   1 10   9
# 10    X
# 11    XI
# 12    XII
# 13    XIII
# 14    XIV
# 49    XLIX (40 + 9)
# 50    L
# 51    LI
# 63    LXIII
#        X=10 L=50 I =1 X 10
#       XL = 40 IX = 9      49

# Please convert *** using DCBA
# 1000      500      100       50      10          5         1
# M         D        C           L      X         V        I
# 50      10     5       1
# D     C    B       A

# Please convert *** using ABCD
#
# A(50)     B(10) C(5)  D(1)

# Please convert *** using CA

# C(5)  A(1)

# Please convert *** using ***
# Please convert III using XVI
# X(10)   V(5) I (1)
# 3   III(3)   3 VVV
# # Please convert CDAC using DCBA
# D 50 C 10 B 5 A 1

# 10 50 1 10 = 40 + 9 = 49
# 49 <==> CDAC

#

# AC
# 1.C(1) A 5
# 2.AC 6


# using CA(C(5) A1
# C(5) A(1)
# AC 4


# ABCCDED
#
# D = 1   E 5
# DED   19
# DED   E (1) D(10)
#
# ABCC              DED
# A(1000)     B(500)    C (100)  D(10)   E(1)

# ABCCDED 1000 + 500 + 200 + 19 1719
# using         ABC_D_E

# 从右向左查找
# ABCADDEFGF
# FGF 第一个和第三个相等，F = 10,G = 1
# FGF = 19
# 490/4900
# 49 abca  c 1* 10**n  c = 1000
# ABCAFDDE ABCA A B(50000) A(10000) C(1000)  D 100 E = 50,F = 10（少了一个5） G =1
# 49000 + 200 + 50 + 19   49269

#               BA_C_DEF_G


# DCBA
# D(50)   C(10)  B(5)  A(1)


# 50: D
# 40: CD
# 10：C
# 9: AC
# 5:B
# 4:AB
# 1:A


# CAC

# 罗马数字转阿拉伯数字
# 1.做法从右向左，一位（最多两位）读取
# C             AC
#  10 +                     AC->9
# BAAA    B  A 1 A 1 A 1



# 49
# 49 >= 50
# 49 >= 40
# 9  >= 10
# 9 >=9 0

# 19
# 19>= 50
# 19>=40
# 19>=10  9
# 9>=9  AC

# CAC

# CAC

# 1.给定一个字符串（ABCD,DCBA,LXVI)
# 2.从右向左读取，标记每个字符的Value
# # I 1 V 5 X 10 L 50 C 100
# # A 1 B 5 C 10 D 50
# # D 1 C 5 B 10 A 50
# 第三步：创建字典
# I  1
# IV 4
# V  5
# IX 9
# X  10
# XL 40
# L  50
# XC 90

# 1 I
# 4 IV
# 5 V


# 第四步，根据创建的字典，去计算对应的数字转换
#


class InvalidProvidedValue(Exception):
    pass


def arabic_to_roman(initial_arabic_number):
    if initial_arabic_number < 1:
        raise InvalidProvidedValue('Initial number must be > 1')
    elif initial_arabic_number > 3999:
        raise InvalidProvidedValue('Initial number must be < 4000')

    result = []
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        while initial_arabic_number >= num:
            initial_arabic_number -= num
            result.append(rom)
    return ''.join(result)


def roman_to_arabic(initial_roman_number):
    initial_roman_number = initial_roman_number.upper()

    result = i = 0
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        l = len(rom)
        while initial_roman_number[i:i+l] == rom:
            result += num
            i += l

    if result == 0:
        raise InvalidProvidedValue('Wrong initial number')
    # `arabic_to_roman` is a way to always get the right value.
    # We should check that it's result is equal to initial value.
    # If not, the result is wrong.
    elif result > 0 and arabic_to_roman(result) != initial_roman_number:
        raise InvalidProvidedValue('Something wrong in initial number')

    return result


def choice_convert_function(number):
    # try convert to integer..
    try:
        return arabic_to_roman(int(number))
    # ..seems to be roman number
    except ValueError:
        return roman_to_arabic(number)

print(arabic_to_roman(5))