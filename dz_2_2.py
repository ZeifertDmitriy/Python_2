# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def Proizved(n, fact = []):
    if n == 1:
        fact.append(n)
    else:
        Proizved(n - 1)
        proizv = 1
        for j in range(len(fact) + 1):
            proizv *= j + 1
        fact.append(proizv)
    return fact
n = input('Введите число: ')
print(Proizved(int(n)))
