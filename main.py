import re

f = open("text.txt", "r", encoding='utf-8')

for s in f:
    result = re.findall(r"\b(([A-Za-zА-Яа-я]+)\2)\b", s)
    #print(result)
    if len(result) != 0:
        result_list = list()
        result_file = open("result.txt", 'a')
        for i in range(0, len(result)):
            result_list.append(result[i][0])
            result_file.write(result[i][0])
            result_file.write(" ")
        result_file.write("\n")
        print(result_list)