# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    if N == 1:
        return 1

    eat_set = {0}
    counter = 1
    while True:
        eat_number = (M * counter) % N
        if eat_number in eat_set:
            return counter
        eat_set.add(eat_number)
        counter += 1