# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    list_length = len(A)
    if list_length >= 3:
        A.sort()
        for index in range(len(A) - 2):
            if A[index] + A[index + 1] > A[index + 2]:
                return 1
        return 0
    else:
        return 0
