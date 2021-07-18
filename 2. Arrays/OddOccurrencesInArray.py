A = [9, 3, 9, 3, 9, 7, 9]


# def solution(A):
#     for i in A:
#         if A.count(i) % 2:
#             return i
#
# print(solution(A))

# works but only scores 66%

# Bitwise XOR solution??

# def solution(A):
#     A.sort()
#     N = len(A)
#     i = 0
#     while i < N:
#         try:
#             if A[i] == A[i + 1]:
#                 i += 2
#             else:
#                 return A[i]
#         except:
#             return A[-1]

# why must it have the else!?

def solution(A):
    A.sort()
    N = len(A)
    i = 0
    while i < N:
        if A[i] == A[i + 1]:
            i += 2
        if A[i] != A[i+1]:
            return A[i]
        else:
            return A[-1]


print(solution(A))