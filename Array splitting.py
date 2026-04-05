n, k = map(int, input().split())
a = list(map(int, input().split()))
 
if k == 1:
    print(a[-1] - a[0])
else:
    diffs = []
    for i in range(1, n):
        diffs.append(a[i] - a[i-1])
    diffs.sort(reverse=True)
    total_cost = a[-1] - a[0]
    saved = sum(diffs[:k-1])   
    print(total_cost - saved)
