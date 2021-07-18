def solution(A):
    Q = len(A) + 1
    B = ((Q * (Q + 1)) // 2)
    return B - sum(A)

# double check me on codility!