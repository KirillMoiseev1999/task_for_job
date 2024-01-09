#Задание 2
def OTA(n):                   #Функция разложения числа на простые множители
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


for num in range(2**29, 2**30):     #Перебор чисел и проверка условия
    l = OTA(num)
    if l[-1] / l[0] >= 100_000_000:
        print(num,l[0], l[-1] )


















'''list_of_prime = [2]
def prime(num): #Функция проверки на простоту
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for num in range(3,2**15,2):
    if prime(num):
        list_of_prime.append(num)

def delim(n):
    d = 2
    c = 0
    while d*d < n:
        if  n % d == 0:
            if d in list_of_prime:
                c += 1
            if (n//d) in list_of_prime:
                c += 1     
        d += 1
    if d*d == n:
        if d in list_of_prime:
            c += 1
    return c

c = 0
for i in range(2, 2**30):
    if delim(i) > 5:
        c+= 1
print(c)'''


'''def prime_fac(n,count=0,prime_num=2):
    if n==1:
        return count
    elif n%prime_num==0:
        return prime_fac(n//prime_num,count+1,prime_num)
    else:
        return prime_fac(n,count,prime_num+1)
    
n = prime_fac(2**32)
print(n)'''