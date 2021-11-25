a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a, b = a / a * b, b / b * a
print(a, b)