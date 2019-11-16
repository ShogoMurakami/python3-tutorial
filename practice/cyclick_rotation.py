# coding: utf-8

# リストの中の数字を右に回転

def solution(A, K):
    return A[-K:] + A[:-K]

A = [3, 8, 9, 7, 6]
K = 3
print(solution(A,K))
