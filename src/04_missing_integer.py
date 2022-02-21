# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    a_set = set(A)
    max_value = max(a_set)
    if max_value <= 0:
        return 1
        
    for i in range(1, max_value + 1):
        if i not in a_set:
            return i

    return max_value + 1
