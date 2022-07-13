# # 1. Напишитепрограмму, которая принимает на вход число N и выдает последовательность из N членов.
# def seach_number(n):
#     res = 1
#     for i in range(n):
#         if i == 0:
#             print(f'{res}', end='')
#         else:
#             res *= -3
#             print(f', {res}', end='')


# n = int(input('Введите число: '))
# seach_number(n)

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество входящей одной строки в другую.
def search_str(str_1, str_2):
    res = 0
    for i in range(len(str_1) - len(str_2) + 1):
        if str_1[i: i + len(str_2)] == str_2:
            res += 1
    print(res)
    return res


str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')
search_str(str_1, str_2)
