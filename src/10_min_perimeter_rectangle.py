# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # write your code in Python 3.6
    if N > 1:
        near_sqrt = int(math.sqrt(N))
        for i in range(near_sqrt, N - near_sqrt):
            if not N % i:
                return (int(N / i) + i) * 2

        return (N + 1) * 2
    else:
        return 4
  