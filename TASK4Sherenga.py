#TASK4#Шеренга
#Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

#Входные данные
#Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.

#from random import randint as r
#count = int(input('Number of students in PhE lesson: '))
#classmate = [r(154, 170) for i in range (count)]
#classmate = sorted(classmate)
#classmate = list(reversed(classmate))
#print(classmate)

#student_hight = int(input('Enter Peter hight: '))

#for j in range(len(classmate)):
 #   if student_hight >= classmate(j):
 #       print(j+1)
 #       break

n = int(input())
list_rost = list()


#2 variant
for i in range(n):
 #   list_rost.append(int(input()))
    k = int(input())
    list_rost.append(k)
    
my_rost = int(input())

j = 1
for i in list_rost:
    if my_rost <= i:
        j += 1
        
print(j)

# Sherenga 2 variant

n = int(input())
list_rost = list()

for i in range(n):
    # list_rost.append(int(input()))
    k = int(input())
    list_rost.append(k)

# имя_списка.sort()
# list2 = sorted(имя_списка)

my_rost = int(input())

j = 1
for i in list_rost:
    if my_rost <= i:
        j += 1

print(j)
