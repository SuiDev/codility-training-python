# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# the other good answer.
def solution(A):
    # write your code in Python 3.6
    n = len(A) + 1
    if n == 1:
        return 1
    expected_sum = (n * (n + 1)) // 2
    return expected_sum - sum(A)
  