# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    leaves_list = []
  
    for i, value in enumerate(A):
        if value not in leaves_list:
            leaves_list.append(value)

        if len(leaves_list) == X:
            return i

    return -1

# the other good answer
"""
def solution(distance, falls):
    if len(falls) == 1 and falls[0] and distance == 1:
        return 0
    elif len(falls) < distance:
        return -1
    positions = set(range(1, distance + 1))
    for minute, pos in enumerate(falls):
        if pos in positions:
            positions.remove(pos)
            if not positions:
                return minute
    return -1
"""
