# coding: utf-8

# リストAの中の孤独な数字を見つける

def solution(A):
     for i in A:
        if A.count(i) == 1:
            return i

A = [9,3,9,3,9,3,9,10]

print(solution(A))
