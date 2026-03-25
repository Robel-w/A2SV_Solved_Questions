t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    max_r = max(0, 0)
    cur = 0
    for x in r:
        cur += x
        max_r = max(max_r, cur)
    
    max_b = 0
    cur = 0
    for x in b:
        cur += x
        max_b = max(max_b, cur)
    
    print(max_r + max_b)
