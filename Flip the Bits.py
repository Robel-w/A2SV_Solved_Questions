t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    if a.count('1') != b.count('1'):
        print("NO")
        continue
    
    balance = 0
    prev = 0
    possible = True
    
    for i in range(n):
        if a[i] == '1':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            match_normal = True
            match_invert = True
            
            for j in range(prev, i + 1):
                if a[j] != b[j]:
                    match_normal = False
                if a[j] == b[j]:
                    match_invert = False
            
            if not match_normal and not match_invert:
                possible = False
                break
            
            prev = i + 1
    
    if possible and prev < n:
        for j in range(prev, n):
            if a[j] != b[j]:
                possible = False
                break
    
    print("YES" if possible else "NO")
