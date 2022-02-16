# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary_data = bin(N)
    binary_str = str(binary_data)[2:]

    start_flag = False
    zero_counter = 0
    zero_count_list = []

    for number in binary_str:
        if number == "1":
            start_flag = True
        
        if start_flag:
            if number == "0":
                zero_counter += 1
            elif number == "1":
                zero_count_list.append(int(zero_counter))
                zero_counter = 0

    return max(zero_count_list)
