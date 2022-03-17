# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    counter = 0
    
    for i in range(1, N + 1):
        if i ** 2 < N:
            if not N % i:
                counter += 2
        elif i ** 2 == N:
            counter += 1
        else:
            break

    return counter
