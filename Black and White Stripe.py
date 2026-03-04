from collections import Counter
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    mp = Counter(s[:k])
    minn = mp['W']

    if k == n:
        minn = mp['W']
    for r in range(k, n):
        if s[r] == 'W':
            mp['W'] +=1

        if s[r-k] == 'W':
            mp['W'] -= 1
        minn = min(minn, mp['W']) 

    print(minn)        
            
