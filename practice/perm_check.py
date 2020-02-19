# coding: utf-8

# 順列なら1を返し、そうでなければ0を返す

def solution(A):

    i = 1
    end = len(A)

    while i <= end:
        if A.count(i) == 0:
            return 0
        i +=1
    else:
        return 1

A = [4,1,3,2,5]

print(solution(A))
