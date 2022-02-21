# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# bad answer
def solution(N, A):
    # write your code in Python 3.6
    counter_list = [0] * N
    for a_value in A:
        if a_value <= N:
            counter_list[a_value - 1] += 1
        else:
            counter_list = [max(counter_list)] * N

    return counter_list

# the other good answer
# countersの全ての要素を最大値に更新する操作を最後にまとめて行う。
"""
def solution(N, A):
    counters = [0] * N
    max_result = 0
    max_counter = 0

    for i in range(len(A)):
        if A[i] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            number_position = A[i] - 1
            if counters[number_position] < max_result:
                counters[number_position] = max_result

            counters[number_position] += 1
            max_counter = max(max_counter, counters[number_position])

    for i in range(N):
        counters[i] = max(max_result, counters[i])

    return counters
"""
