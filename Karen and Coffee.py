n, k, q = map(int, input().split())
 
maxx = 200001
diff = [0] * maxx
 
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    if r + 1 < maxx:
        diff[r + 1] -= 1
 
cover = [0] * maxx
current = 0
for i in range(1, maxx):
    current += diff[i]
    cover[i] = current
 
prefix = [0] * maxx
for i in range(1, maxx):
    prefix[i] = prefix[i-1] + (1 if cover[i] >= k else 0)
 
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])
    
