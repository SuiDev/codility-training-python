# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    if not A % K:
        return (B - A) // K + 1

    return (B - (A - A % K)) // K
