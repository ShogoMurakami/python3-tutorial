# coding: utf-8

# 2D List

n = int(input())

s = [input().split() for i in range(n)]

for j in s:
    for k in j:
        print(k)

print(s)
