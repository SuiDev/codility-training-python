# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    # write your code in Python 3.6
    sum = 0
    max_sum = -sys.maxsize
    for value in A:
        sum = max(value, sum + value)
        max_sum = max(max_sum, sum)

    return max_sum
