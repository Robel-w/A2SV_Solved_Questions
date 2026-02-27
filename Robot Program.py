t = int(input())
for _ in range(t):
        n, x, k  =map(int, input().split())
        s = input()
        first_hit_time = -1
        current_pos = x
        for i in range(min(n, k)):
            if s[i] == 'L':
                current_pos -= 1
            else:
                current_pos += 1
            
            if current_pos == 0:
                first_hit_time = i + 1
                break
        
        if first_hit_time == -1:
            print(0)
            continue
            
        cycle_time = -1
        current_pos = 0
        for i in range(n):
            if s[i] == 'L':
                current_pos -= 1
            else:
                current_pos += 1
            
            if current_pos == 0:
                cycle_time = i + 1
                break
        
        remaining_time = k - first_hit_time
        
        if cycle_time == -1:
            print(1)
        else:
            print(1 + (remaining_time // cycle_time))



