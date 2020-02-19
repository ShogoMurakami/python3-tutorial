# coding: utf-8

n = input().split()

s =[input().split() for i in range(int(n[0]))]

for (number, j) in enumerate(s):
    result = int(j[0]) - (int(j[1]) * 5 )

    if result < 0:
        result = 0

    if result >= int(n[1]):
        print(number + 1)
    
