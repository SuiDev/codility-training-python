# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# bad answer
def solution(A):
    # write your code in Python 3.6
    appearance_element = set(A)
    for element in appearance_element:
        if A.count(element) % 2:
            return element

# good answer
"""
def solution(A):
    n = len(A)

    if n == 1:
        return A[0]
    result = 0

    # 同じ要素同士で排他的論理和を取ると打ち消しあい、奇数の要素の値が残る。
    # MEMO: <https://stackoverflow.com/questions/52885716/finding-the-odd-integer-that-does-not-form-the-pair-in-the-list>
    for i in range(0, n):
        result ^= A[i]
    return result
"""
