# coding: utf-8

now = input().split()

n = int(input())

s = [input().split() for i in range(n)]

result_list = []
check_number = 0

for j in s:
    if int(j[1]) <= int(now[0]) and int(j[2]) >= int(now[0]) and int(j[3]) <= int(now[1]) and int(j[4]) >= int(now[1]) and int(j[5]) <= int(now[2]) and int(j[6]) >= int(now[2]):
        result_list.append(j[0])
    else:
        result_list.append(False)

for k in result_list:
    if k != False:
        print(k)
        check_number += 1

if check_number == 0:
    print("no evolution")
