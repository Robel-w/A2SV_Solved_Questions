n, s = map(int, input().split())
a = list(map(int, input().split()))

count = 0
summ = 0
r = 0
for l in range(n):
    while r < n and summ < s:
        summ += a[r]
        r += 1
    if summ >= s:
        count += (n - r + 1)

    summ -= a[l]

print(count)
