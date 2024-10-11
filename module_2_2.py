first = int(input('Введите первое число: '))
second  = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('Равны 3 числа')
elif first == second or first == third or second == third:
    print('Равны 2 числа')
else: print('Равных чисел нет')