year = int(input('Введите год '))
if ((year % 100) // 10) == 0 and (year % 10) == 0:
    print ('yes')
else:
    print ('no')
