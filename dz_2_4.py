#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

n = int(input('Введите число: '))
list = []
for i in range(n):
    list.append(randint(-n,n))
print(list)
file_text = open('file.txt','r')
sum = 0
while True:
    line = file_text.readline()
    if not line:
        break
    if int(line.strip()) < len(list):
        sum += list[int(line.strip())]
file_text.close()
print(sum)