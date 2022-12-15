#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

#a = int(input("Введите число: "))
#с = 0
#if  10**4 >= a and a > 0:
#    sum = (a + 1) * a /22
#elif a < 0 and a > (-1) * 10**4:
#    sum = (a - 1) * a / 2 * (-1)
#print(f'Summ of whole numbers from 1 to {a} равна "',int(sum), '"')

N = int(input(" Ввведите число: "))
i = 1
s = 0
while i <= N:
    s = i + s
    i = i + 1
print(f'Sum of digits from 1 to {N} = "',int(s), '"')

# 2. Сумма

#n = int(input())
#flag = True
#if n < 0:
#    flag = False
#n = abs(n)
#if flag:
#    print(int(((n + 1) / 2) * n))
#else:
#    print(-int(((n + 1) / 2) * n) + 1)

# 5
# 1 + 2 + 3 + 4 + 5 = 15
# -5 
# 1 + 0 - 1 - 2 - 3 - 4 -5 = -14 (15 -> -15 -> +1 -> -14)

   