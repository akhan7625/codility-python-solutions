A = [3, 4, 3, 2, 3, -1, 3, 3]


def solution2(A):
    N = len(A)
    dom = 0
    dom_count = 0
    dom_index = 0
    for i in range(N):
        if dom_count == 0:
            dom = A[i]
            dom_index = i
            dom_count += 1
        else:
            if A[i] == dom:
                dom_count += 1
            else:
                dom_count -= 1
    if len([num for num in A if num == dom]) <= N // 2:
        return -1
    else:
        return dom_index

# def solution(A):
#     N = len(A)
#     dom_min = N / 2
#     for i, value in enumerate(A):
#         cur_max_count = A.count(value)
#         if N == 0:
#             return -1
#         elif cur_max_count > dom_min:
#             return i
#     return -1
#
#
# print(solution(A))

# only received 83% score due to time out errors below

# ▶medium_pyramid
# decreasing and plateau, medium✘TIMEOUT ERROR
# running time: 0.752 sec., time limit: 0.192 sec.
# ▶large_pyramid
# decreasing and plateau, large✘TIMEOUT ERROR
# Killed. Hard limit reached: 6.000 sec.

# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
#
# For example, consider array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
# Write a function
#
# def solution(A)
#
# that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.
#
# For example, given array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
