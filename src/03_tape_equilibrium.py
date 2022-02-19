# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result = abs(sum(A[:1]) - sum(A[1:]))

    for i in range(1, len(A) - 1):
        result = min(result, abs(sum(A[:i+1]) - sum(A[i+1:])))

    return result

# the other good answer.
"""
def solution(nums):
    lefts, rights = sum(nums[:1]), sum(nums[1:])
    minval = abs(lefts - rights)
    for i in range(1, len(nums) - 1):
        # 今までの計算を繰り返さないように書く
        lefts += nums[i]
        rights -= nums[i]
        minval = min(minval, abs(lefts - rights))
    return minval
"""