# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    # write your code in Python 3.6
    dominator = int(len(A) / 2)

    a_collection = collections.Counter(A)
    for key, value in a_collection.items():
        if dominator < value:
            for index, a in enumerate(A):
                if key == a:
                    return index

    return -1 

# the other good answer.
"""
def solution(A):
    if len(A) == 0:
        return -1

    sort_a = sorted(A)
    l = len(A) // 2
    domi_candidate = sort_a[l]
    if A.count(domi_candidate) > l:
        return A.index(domi_candidate)
    return -1
"""