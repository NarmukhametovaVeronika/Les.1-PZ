while True:
    a = float(input("Начальный результат(км):  "))
    b = float(input("Конечный результат(км):  "))
    if a < 0 or b < 0:
        print("Введите положительные числа")
    else:
        days = 1
        while a < b:
            a += a * 0.1
            days += 1
            print(f"Спортсмен добьётся успеха за {days} дней.")
            break