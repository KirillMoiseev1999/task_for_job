#Задание 3
def prime(n): #Создадим функцию проверки на простту 
    if n == 2:
        return True
    if n % 2  == 0 or n == 1:
        return False
    d = 3
    while d*d < n:
        if n % d == 0:
            return False
        d += 2
    if d*d == n:
        return False
    return True


prime_nums = [] 
for i in range(2,10**6+1): #Сгенерируем массив простых чисел до 1 миллиона
    if prime(i):
        prime_nums.append(i)

super_prime_nums = []
for i in range( len(prime_nums)): #Сгенерируем массив супер простых чисел до 1 миллиона
    if prime(i+1):
        super_prime_nums.append(prime_nums[i])

count = 0 
for i in range(len(super_prime_nums)): #Посчитаем сколько супер простых чисел больших 448
    if super_prime_nums[i] > 448:
        count += 1    
print(count)
    

