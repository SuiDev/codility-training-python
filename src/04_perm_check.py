# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    # write your code in Python 3.6
    A_collections = collections.Counter(A)
    for col in A_collections:
        if A_collections[col] != 1:
            return 0

    max_value = max(A)
    return 1 if max_value == len(A) and A.count(max_value) == 1 else 0
