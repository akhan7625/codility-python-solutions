def solution(N):
    if N > 0:
        N = bin(N)
        trail_removed = N[2:].rstrip('0').split('1')
        max_gap = max(trail_removed)
        return int(len(max_gap))
    else:
        return 0
    pass


# solution 2

def second_solution(N):
    x = bin(N)
    y = x[2:]
    accum = 0
    max_gap = 0

    for i in y:
        if i == '0':
            accum += 1
        elif i == '1':
            if accum > max_gap:
                max_gap = accum
            accum = 0
    return max_gap
    pass