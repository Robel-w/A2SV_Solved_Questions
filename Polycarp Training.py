n = int(input())

arr = list(map(int, input().split()))
arr.sort()
pos =1
for i in range(n):
    if arr[i] >= pos:
        pos += 1
print(pos - 1) 
