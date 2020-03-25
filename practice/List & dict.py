

#合并两个字典
dict1 ={1:1}
dict2 ={2:2}
dict1.update(dict2)
print(dict1)

#字典插入key：value
dict3 = {}
dict1[5]=4#key in [], so 5 is the key, 4 is the value
print(dict1)

#字典插入字典

dict1 ={1:1}
dict2 ={2:2}
dict3[1]={2:2}
print(dict3)

#用append or extend(这个用于list，往dict里面添加ele时，用update) 时候，dict里面必须已经有元素
#如果没有元素，需要import defaultdict
from collections import defaultdict
dict1={}
dict1[1]=[1]
print("情况1",dict1)

#定义dict2的value是list

dict2=defaultdict(list)
dict2[1].append(1)
print("情况2",dict2)

#defaultdict 添加 dict
dict3=defaultdict(dict)
dict3[1].update({2:2})
print("情况3",dict3)

#取出字典中的key作为list
dict4={1:3,2:8,3:4}
print("list key:",dict4.keys())


# 取出list的第一位数字
cycles_key=[1,2,3,4]
first_number = cycles_key[0]
print("first number of list:",first_number)

#取出第一个数字对应的的value
mapping={1:2,2:4,3:8}
first_number2 = mapping[first_number]
print("first value of dict:",first_number2)
#取出某个key的value
print("list value of 1-key:",mapping[1])
print("list value of 1-key:",mapping.get(1))
# 从value取Key
print("list key of value-2",mapping)

#字典的value是list
dict5 = {"a":[1,2],"b":[3,4],"c":[5,6]}
x,y = dict5["a"]
print("x:",x)
print("y:",y)


#dict删除
dict6 = {"a":[1,2],"b":[3,4],"c":[5,6]}
del dict6["a"]
print("dict6:",dict6)
#字典出现重复，会只显示最后一个结果
dict7 = {"a":[1,2],"a":[3,4],"c":[5,6]}
print("dict7:",dict7)


#拆分一个单词
roman = "apple"
roman_list = list(roman)
print(roman_list)

# 确定元素的index
list=[1,2,3,4]
a=list.index(1)
print("index:",a)