from collections import Counter
n, m = map(int, input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))
mpa = Counter(a)
mpb = Counter(b)
res = 0
for key, val in mpa.items():
    if key in mpb:
        res += val * mpb[key]

print(res)
