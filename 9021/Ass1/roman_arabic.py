import re
from collections import Counter
try:
    name_of_file = input("How can I help you? ")
except ValueError:
    print("I don't get what you want, sorry mate!")
    sys.exit()
input_list = name_of_file.split(" ")
word_dic = {'0': 1, '1': 5, '2': 10, '3': 50, '4': 10**2, '5': 5*10**2, '6': 10**3, '7':5*10**3, '8':10**4, '9':5*10**4,'10':10**5,'11':5*10**5,'12':10**6,'13':5*10**6,
                '14':10**7,'15':5*10**7,'16':10**8,'17':5*10**8,'18':10**9,'19':5*10**9,'20':10**10,'21':5*10**10,'22':10**11,'23':5*10**11,'24':10**12,'25':5*10**12,
                '26':10**13,'27':5*10**13,'28':10**14,'29':5*10**14,'30':10**15,'31':5*10**15,'32':10**16,'33':5*10**16,'34':10**17,'35':5*10**17,'36':10**18,
                '37':5*10**18,'38':10**19,
                '39':5*10**19,'40':10**20,'41':5*10**20,'42':10**21,'43':5*10**13,'44':10**22,'45':5*10**22,'46':10**23,'47':5*10**23,'48':10**24,'49':5*10**24,'50':10**25,
                '51':5*10**25,'52':10**26}
ARABIC_TO_ROMAN = {"Z":5*10**16,"Y":10**16,"X":5*10**15,"W":10**15,"V":5*10**14,"U":10**14,"T":5*10**13,"S":10**13,"R":5*10**12,"Q":10**12,"P":5*10**11,"O":10**11,"N":5*10**10,"M":10**10,"L":5*10**9,"K":10**9,
                   "J":5*10**8,"I":10**8,"H":5*10**7,"G":5*10**6,"F":1000000,"E":500000,"D":100000,"C":50000,"B":10000,"A":5000,
                   "M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
class Solution1(object):
    def intToRoman(self, num: int) -> str:

           k = ['', 'k', 'kk', 'kkk']
           i = ['', 'i', 'ii', 'iii', 'ij', 'j', 'ji', 'jii', 'jiii', 'ik']
           g = ['', 'g', 'gg', 'ggg', 'gh', 'h', 'hg', 'hgg', 'hggg', 'gi']
           e = ['', 'e', 'ee', 'eee', 'ef', 'f', 'fe', 'fee', 'feee', 'eg']
           c = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'ce']
           a = ['', 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'bc']
           Z = ['', 'Z', 'ZZ', 'ZZZ', 'Za', 'a', 'aZ', 'aZZ', 'aZZZ', 'Zb']  # 0, 100, 200, ... , 900
           x = ['', 'x', 'xx', 'xxx', 'xY', 'Y', 'Yx', 'Yxx', 'Yxxx', 'xZ']  # 0, 1, 2, ... , 9
           V = ['', 'v', 'vv', 'vvv', "vW", "W", "Wv", "Wvv", 'Wvvv', 'vx']  # 0,10000,20000,30000,40000,50000
           T = ['', 'T', 'TT', 'TTT', 'TU', 'U', 'UT', "UTT", 'UTTT', 'Tv']  # 0, 1000, 2000, 3000 ,4000, 5000... 9000
           R = ['', 'R', 'RR', 'RRR', 'RS', 'S', 'SR', 'SRR', 'SRRR', 'RT']  # 0, 100, 200, ... , 900
           P = ['', 'P', 'PP', 'PPP', 'PQ', 'Q', 'QP', 'QPP', 'QPPP', 'PR']  # 0, 10, 20, ... , 90
           N = ['', 'N', 'NN', 'NNN', 'NO', 'O', 'ON', 'ONN', 'ONNN', 'NP']  # 0, 1, 2, ... , 9
           l = ['', 'l', 'll', 'lll', "lm", "m", "ml", "mll", "mlll", "lN"]  # 0,10000,20000,30000,40000,50000
           J = ['', 'J', 'JJ', 'JJJ', 'JK', 'K', "KJ", "KJJ", "KJJJ", "JL"]  # 0, 1000, 2000, 3000 ,4000, 5000... 9000
           H = ['', 'H', 'HH', 'HHH', 'HI', 'I', 'IH', 'IHH', 'IHHH', 'HJ']  # 0, 100, 200, ... , 900
           F = ['', 'F', 'FF', 'FFF', 'FG', 'G', 'GF', 'GFF', 'GFFF', 'FH']  # 0, 10, 20, ... , 90
           D = ['', 'D', 'DD', 'DDD', 'DE', 'E', 'ED', 'EDD', 'EDDD', 'DF']  # 0, 1, 2, ... , 9
           B = ['', 'B', 'BB', 'BBB', "BC", "C", "CB", "CBB", 'CBBB', 'BD'] #0,10000,20000,30000,40000,50000
           M = ['', 'M', 'MM', 'MMM', 'MA', 'A', 'AM', "AMM", 'AMMM', 'MB']  # 0, 1000, 2000, 3000 ,4000, 5000... 9000
           C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']  # 0, 100, 200, ... , 900
           X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']  # 0, 10, 20, ... , 90
           I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']  # 0, 1, 2, ... , 9

           return  N[(num % 10**11)// 10**10] +l[(num % 10**10)// 10**9] + J[(num % 10**9)// 10**8] +H[(num % 10**8)// 10**7] +F[(num % 10**7)// 10**6] + D[(num % 10**6)// 10**5] + B[(num % 10**5)// 10**4] + M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

roman = Solution1()


class Solution2(object):
    def isValid(self, left, right):
        if left == "I" and (right == "V" or right == "X"):
            return True
        if left == "X" and (right == "L" or right == "C"):
            return True
        if left == "C" and (right == "D" or right == "M"):
            return True
        return False

    def romanToInt(self, s: str) -> int:
        n = len(s)
        if n <= 0:
            return 0
        merge_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        ans = 0
        while (i < n - 1):
            if (merge_dic[s[i]] >= merge_dic[s[i + 1]]):
                ans = ans + merge_dic[s[i]]
                i += 1
            elif (merge_dic[s[i]] < merge_dic[s[i + 1]]):
                if self.isValid(s[i], s[i + 1]):
                    ans = ans + merge_dic[s[i + 1]] - merge_dic[s[i]]
                    i += 2
                else:
                    return 0
        if i == n - 1:
            ans = ans + merge_dic[s[i]]
        return ans

ans = Solution2()

if len(input_list)<3:
    print("I don't get what you want, sorry mate!",end='')
exit()
a = input_list[0]
b = input_list[1]
c = input_list[2]

def check_num(number):
    number = str(c)
    value = re.compile(r'^[0]')
    result = value.match(number)
    if result:
        return True
    elif int(c)>3999 and len(input_list)==3:
        return True
    else:
        return False

def check_str(roman):
    roman=str(c)
    index_roman1 = roman.find("IIII")
    index_roman2 = roman.find("XXXX")
    index_roman3 = roman.find("CCCC")
    index_roman4 = roman.find("LL")
    index_roman5 = roman.find("VV")
    index_roman6 = roman.find("DD")
    index_roman7 = roman.find('IVI')
    index_roman8 = roman.find('IVX')

    if index_roman1 > 0 or index_roman2 > 0 or index_roman3 > 0 or index_roman4 > 0 or index_roman5 > 0 or index_roman6 >0 or index_roman7>0 or index_roman8 > 0:
        return True
    else:
        return False

def convert(n):
    rule_list = list(input_list[-1])#第二个指定规则的字符串
    rule_dic = {}
    for i in range(len(rule_list)):
        rule_dic[rule_list[-1 - i]] = word_dic[str(i)]
    if c.isdigit():
       roman_num = roman.intToRoman(int(c))
       roman_list = list(roman_num)
       new_roman=[]
       for i in roman_list:
            new_dict = {value: key for key, value in rule_dic.items()}
            new_int = ARABIC_TO_ROMAN.get(i)
            new_key = new_dict[new_int]
            new_roman.append(new_key)
            continue
       return "".join(new_roman)
    else:
        convert_list = list(c)
        convert_num = 0
        for i in convert_list:
            if i in word_dic:
                convert_num += rule_dic[i]
                return convert_num
            elif i in ARABIC_TO_ROMAN:
                convert_roman=[]
                conver_ab = rule_dic[i]
                convert_roman.append(roman.intToRoman(conver_ab))
                continue
                return "".join(new_roman)
            else:
                print("Hey, ask me something that's not impossible to do!",end='')
                break
                convert_num += rule_dic[i]
                return convert_num


def check_pattern1(a, b, c):
    if len(input_list) == 3:
        if input_list[0] == "Please" and input_list[1] == "convert" and len(input_list) == 3:
            return True
        else:
            return False
    elif len(input_list) == 5:
        if input_list[0] == "Please" and input_list[1] == "convert" and input_list[3] == "using" and len(
                input_list) == 5:
            return True
        else:
            return False
    elif len(input_list) == 4:
        if input_list[0] == "Please" and input_list[1] == "convert" and input_list[3] == "minimally" and len(
                input_list) == 4:
            return True
        else:
            return False
    else:
        return False


if check_pattern1(a, b, c):
    if c.isdigit():
        if check_num(c):
            print("Hey, ask me something that's not impossible to do!",end='')
        else:
            if len(input_list)== 5:
                print("Sure! It is", convert(c), end='')
            else:
                print("Sure! It is", roman.intToRoman(int(c)),end='')
    elif type(c) == str:
        if check_str(c):
            print("Hey, ask me something that's not impossible to do!",end='')
        else:
            if len(input_list) == 5:
                if convert(c) == None:
                   pass
                else:
                    print("Sure! It is", convert(c),end='')
            else:
                print("Sure! It is", ans.romanToInt((c)),end='')
    else:
        print("I don't get what you want, sorry mate!",end='')

else:
    print("I don't get what you want, sorry mate!",end='')
