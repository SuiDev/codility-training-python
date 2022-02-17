# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# my answer
def solution(A, K):
    # write your code in Python 3.6
    repeat_count = int(K)

    if len(A) >= 2:
        for i in range(repeat_count):
            A = [A[-1]] + A[0:-1]

    return A

"""
# the other good answer
def solution(A, K):
    n = len(A)
    B = [None] * n
    for i in range(0, n):
        B[(i + K) % n] = A[i]
    return B
"""
