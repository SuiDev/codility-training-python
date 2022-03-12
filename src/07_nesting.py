# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    for value in S:
        if value == ")":
            if "(" in stack:
                stack.pop()
            else:
                return 0
        elif value == "(":
            stack.append(value)
            
    return 0 if stack else 1
