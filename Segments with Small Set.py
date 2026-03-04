from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

mp = defaultdict(int)
left = 0
distinct = 0
count = 0

for right in range(n):
    if mp[a[right]] == 0:
        distinct += 1
    mp[a[right]] += 1

    while distinct > k:
        mp[a[left]] -= 1
        if mp[a[left]] == 0:
            distinct -= 1
        left += 1

    count += (right - left + 1)

print(count)
