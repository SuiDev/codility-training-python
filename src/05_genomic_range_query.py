# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    result = []

    for i in range(len(P)):
        slice_letters = S[P[i]:Q[i]+1]

        if "A" in slice_letters:
            result.append(1)
            continue

        if "C" in slice_letters:
            result.append(2)
            continue

        if "G" in slice_letters:
            result.append(3)
        else:
            result.append(4)

    return result
    