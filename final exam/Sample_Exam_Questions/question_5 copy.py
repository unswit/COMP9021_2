# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    max_inf = -1000
    #将查询年度中12个月对应的inflat按照月份顺序放进inflation，然后找到最大的float，
    #因为1个月1个float，所以每年的inflation表格会有12个float所处的位置是 (第几位+1)那就是几月份
    inflation =[]
    maxMonths=''
    #先打开cpiai
    with open ('cpiai.csv','r') as csv_file:
        #读取其中数据，delimiter=是分隔符，csv对应的分隔符是“，”
        csv_reader=csv.reader(csv_file,delimiter=",")
        row_count =0
        #开始逐行读取
        for row in csv_reader:
            #第一行是标题，所以不用读取
            if row_count == 0:
                row_count =1
            else:
                #需要取出行的年份和inflation
                #每个row读出来的样子是['1972-08-01','42.0','0.24'],⚠️注意跟csv打开看的样式不一样，csv日期显示8/1
                #年份的位置是：row中的 第[0]位，然后将第[0]位按照‘-’分割后的新字符串中的第[0]位
                if row[0].split('-')[0] == str(year):
                    #float的位置是row的第[2]位
                    #如果此刻的float是最大的，那max_int就取此时此刻的float
                    if float(row[2])>max_inf:
                        max_inf = float(row[2])
                    #把所有的float都扔到infaltion里
                    inflation.append(float(row[2]))
                    
    #用索引i遍历inflation中12个float，因为inflation的索引可以用于对应到months中的月份
    for i in range(len(inflation)):
        # inflation中的float = max_inf中记录的最大float
        if inflation[i]==max_inf:
            #就把months中相同索引i位置对应的月份放入maxMonths中去
            maxMonths +=months[i]+', '
    
    print('In '+str(year)+', maximum inflation was:', max_inf)
    print('It was achieved in the following months: '+maxMonths[:-2])
        
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()

