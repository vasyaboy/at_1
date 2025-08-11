def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    number = int(input("Введите число для вычисления факториала: "))
    if number < 0:
        print("Факториал определен только для неотрицательных чисел!")
    else:
        result = factorial(number)
        print(f"Факториал числа {number} равен {result}")
except ValueError:
    print("Пожалуйста, введите целое число!")