weight = int(input('Введите вес боксера '))
if x<60:
    print('Легкий вес')
elif x>=60 and x<64:
    print('Первый полусредний вес')
elif x<=69:
    print('Полусредний вес')
else:
    print('Боксер слишком жирный')
