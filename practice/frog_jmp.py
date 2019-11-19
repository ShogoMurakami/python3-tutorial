# coding: utf-8k

def solution(X, Y, D):

    times = 0

    while X < Y:
        X += D
        times += 1

    else:
        return times


X = 10
Y = 85
D = 30

print(solution(X, Y, D))
