# COMP9021 Practice 2 - Solutions


'''
Decodes all multiplications of the form

                       *  *  *
                  x       *  *
                    ----------
                    *  *  *  *
                    *  *  *
                    ----------
                    *  *  *  *

such that the sum of all digits in all 4 columns is constant.
'''


#x是三位数，所以取值范围在100到1000
for x in range(100, 1_000):
    #y是2位数，取值范围10-100之间
    for y in range(10, 100):
        #第三行的product0:是y的个位乘以x。
        #y的个位等于y除以10的余数
        product0 = x * (y % 10)
        #product0是四位数，范围应该大于等于1000，如果小于1000则跳出本次循环
        if product0 < 1_000:
            continue
        #product1是y的十位乘以x
        #y的十位等于y//10
        product1 = x * (y // 10)
        #product1是三位数，所以范围应该小于1000，如果大于1000则跳出本次循环
        if product1 >= 1_000:
            continue
        # total等于product0 + product1*10
        total = product0 + 10 * product1
        #total是四位数，应该大于1000，小于10_1000，如果大于10_000则跳出本次循环
        if total >=10_000:
            continue
        # 纵列的合计数等于 x的个位+y的个位+product0的个位+total的十位
        the_sum = x % 10 +y % 10 + product0 % 10 + total % 10
        #如果 x的十位 + y的十位+ product0的十位+ product1的十位+total的十位
        if x // 10 % 10 + y // 10 + product0 // 10 % 10 + product1 % 10 + total // 10 % 10 !=\
                                                                                            the_sum:
                continue
        if x // 100 + product0 // 100 % 10 + product1 // 10 % 10 + total // 100 % 10 != the_sum:
            continue
        if product0 // 1_000 + product1 // 100 + total // 1_000 == the_sum:
            print(f'{x} * {y} = {total}, all columns adding up to {the_sum}.')
