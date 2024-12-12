import re #импортируем модуль для регулярных выражений

f=open("24.txt") #открываем файл
text=f.readline() #считываем файл
match=r'((([+][7]{1})|[8]{1})\d{10})' #регулярное выражение для номеров телефона
numbers=re.findall(match, text) #запись номеров телефона в массив
count=0


for i in range(len(numbers)):
    #проверяем начинается ли номер с +7, если да то проверяем наличие строки 777 в срезе строки с третьего символа
    if numbers[i][0][0]=="+":
        if "777" in numbers[i][0][2:]:
            count+=1

    else:
        if "777" in numbers[i][0]:
            count+=1
print(count)







