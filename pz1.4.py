n = abs(int(input("Загадайте целое положительное число: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра загаданного числа ", max)
        break