# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    # write your code in Python 3.6
    min_value = sys.maxsize
    max_value = 0
    for a in A:
        min_value = min([min_value, a])
        max_value = max([max_value, a - min_value])
    return max_value
