#Задание 1
l = [] #Будующий список с номерами агентов
def prime(num): #Функция проверки на простоту
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for num in range(2,100): #Генератор кодов агентов
    if prime(num):
        if num < 10:
            l.append('00'+str(num))
        else:
            l.append('0'+str(num))

for code1 in l:  #Генератор масок и проверка подходящих и сразу вывод
    for s in '0123456789':
        for code2 in l:
            mask = '1' + code1 + s + code2 + '1'
            if ( int(mask) % 1961== 0 )  and  ( int(mask)<10**9 ):
                print(mask, int(mask)// 1961)

    
    
    