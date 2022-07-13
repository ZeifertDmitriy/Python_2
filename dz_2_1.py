# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def sum_number(n):
    res = 0
    for i in range(len(n)):
        if n[i].isdigit() == True:
            res += int(n[i])
    print(res)
n = input('Введите вещественное число: ')
sum_number(n)