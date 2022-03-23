# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    abstract_list = []
    for index, a in enumerate(A):
        if a < 0:
            abstract_list.append(abs(a))
        else:
            abstract_list += A[index:]
            break
            
    return len(set(abstract_list))
  