for _ in range(int(input())):
    s = input()
    keys = set()
    i = 0
    
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2  
        else:
            keys.add(s[i])
            i += 1
            
    print("".join(sorted(keys)))
