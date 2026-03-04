n, s = map(int, input().split())
a = list(map(int, input().split()))

count = 0
l = 0
summ = 0
for r in range(n):
    summ += a[r]
    
    while summ > s and l <= r:
        summ -= a[l]
        l += 1       
    count += (r - l + 1)
    
print(count)
