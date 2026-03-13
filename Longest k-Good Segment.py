n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = 0
mp = {}
maxx = 0 
s =[1,1]
for r in range(n):
    mp[a[r]] = mp.get(a[r],0) + 1

    while len(mp) > k:
        
        mp[a[l]] -= 1
        if mp[a[l]] == 0:
            del mp[a[l]]
        l +=1

    if r-l > maxx:
        maxx = r-l
        if s:
            s.pop()
            s.pop()
        s.append(l+1)
        s.append(r+1)

print(*s)

        
     
    
            
