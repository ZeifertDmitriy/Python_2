# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
def Posledov(n):
    spisok = []
    sum = 0
    for i in range(n):
        spisok.append((1 + 1 / (i + 1)) ** (i + 1))
        sum += spisok[i]
        i += 1
    print(spisok)
    return sum
n = input('Введите число: ')
print(Posledov(int(n)))