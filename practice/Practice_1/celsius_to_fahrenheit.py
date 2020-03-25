

min_temperature = 0
max_temperature = 100
step = 10

print('Celsiust\Fahrenheit')

for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = celsius*9/5 +32
    print(f'{int(fahrenheit)}\t{int(celsius)}')

