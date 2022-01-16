def solution(A):
    B = set(sorted(A))
    A = set(range(1,10001))
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m
