n= int(input())
par = []
for _ in range(n-1):
    a = int(input())
    par.append(a)
children =[[] for _ in range(n+1)]
for ind, val in enumerate(par):
    child = ind +2
    children[val].append(child)

for i in range(1, n+1):
    if not children[i]:
        continue    
    child_count = 0   

    for child in children[i]:
        if not children[child]:
            child_count +=1
    if child_count < 3:
        print('No')
        exit()
print('Yes')
