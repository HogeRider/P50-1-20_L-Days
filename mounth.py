year = int(input('Введите год: '))
CheckYear = int(0) #0 не високосный | 1 високосный
if year % 4 != 0:
    print('Год не високосный.')
    CheckYear = 0

elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
        CheckYear = 1
    else:
        print('Год не високосный.')
        CheckYear = 0
else:
    print('Год високосный.')
    CheckYear = 1

daysNevisokosniy = [31,28,31,30,31,30,31,31,30,31,30,31]
daysVisokosniy = [31,29,31,30,31,30,31,31,30,31,30,31]

counter = 0
sum = 0
day =""

if CheckYear==0:
    while counter !=12:
        day = daysNevisokosniy[counter]
        counter +=1
        for i in range (1, day+1):
            if i >=10:
                num1, num2 = divmod(i, 10)
                sum += num1 + num2
            if i <10:
                sum += int(i)
else:
    while counter !=12:
        day = daysVisokosniy[counter]
        counter +=1
        for i in range (1, day+1):
            if i >=10:
                num1, num2 = divmod(i, 10)
                sum += num1 + num2
            if i <10:
                sum += int(i)
print(sum)






