# 5. Реализуйте алгоритм перемешивания списка.
file_text = open('file.txt','r+')
list = []
list.append('')
i = 0
for line in file_text:
    list.append(line.strip())
    i += 1
list[0] = list[i]
list.pop(i)
file_text.close()
file_text = open('file.txt','w')
for i in range(len(list)):
    if i  == 0:
        file_text.write(list[i])
    else:
        file_text.write('\n' + list[i])
file_text.close()
print(list)