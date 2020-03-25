# COMP9021 Practice 8 - Solutions


'''
Prompts the user for an amount, and outputs the minimal number of banknotes needed
to match that amount, as well as the detail of how many banknotes of each type value are used.

The available banknotes have a face value which is one of $1, $2, $5, $10, $20, $50, and $100.
'''
N = int(input("Input the desired amount: "))

#字典
banknotes_value=[100,50,20,10,5,2,1]
banknotes = dict.fromkeys(banknotes_value,0)

index = 0
while N>0 and index <len(banknotes):
    count,N = divmod(N,banknotes_value[index])
    if count >0:
        banknotes[banknotes_value[index]]=count
    index +=1

print('The detail is:')
for value in banknotes:
    if banknotes[value]:
        print(f' {"$"+str(value):>4}:{banknotes[value]}')
        
    
