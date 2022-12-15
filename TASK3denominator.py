#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

#Входные данные
#Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

n = int(input())
i = 1
while i <= n:
    i = i + 1
    if n % i == 0:
        print(i)
        break
    
 # минимальный делитель
#n = int(input())
#flag = True
#i = 2
#while flag:
 #   if n % i == 0:
 #       print(i)
 #       flag = False
 #   i += 1
