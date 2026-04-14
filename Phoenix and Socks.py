from collections import Counter

t = int(input())
for _ in range(t):
    N, L, R = map(int, input().split())
    C = list(map(int, input().split()))
    
    lcnt = [0] * (N + 1)
    rcnt = [0] * (N + 1)
    
    for i in range(N):
        if i < L:
            lcnt[C[i]] += 1
        else:
            rcnt[C[i]] += 1
    
    for i in range(1, N + 1):
        mn = min(lcnt[i], rcnt[i])
        lcnt[i] -= mn
        rcnt[i] -= mn
        L -= mn
        R -= mn
    
    if L < R:
        lcnt, rcnt = rcnt, lcnt
        L, R = R, L
    
    ans = 0  
    for i in range(1, N + 1):
        extra = L - R
        can_do = lcnt[i] // 2
        do = min(can_do * 2, extra)
        ans += do // 2
        L -= do
    
    ans += (L - R) // 2 + (L + R) // 2
    print(ans)
