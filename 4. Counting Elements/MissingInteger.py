A = [1, 3, 6, 4, 1, 2]
# the above should return 5

B = [1, 2, 3]
# the above should return 4

C = [-1, -3]
# the above should return 1

def solution(A):
    return min(set(range(1, len(A)+2)).difference(set(A)))

# comparing a set (ordered, unique values only) with a range from 1 to 2 more than the length
# of the array we're comparing with. It will return the minimum number in the first set that is different from
# in set(A)

print(solution(A))

# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].