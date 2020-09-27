n = int(input())
bridges = []    #(h, x_start, x_end)
for i in range(n):
    input()     #eliminate '\n'
    bridges.append(tuple(map(int, input().split())))
bridges.sort(key = lambda x:x[1])
blocks = bridges[0][0]
bridge = 0
for i in range(2, bridges[-1][-1] + 1):
    if bridges[bridge][1] < i < bridges[bridge][2]:
        blocks += 1
    else:
        blocks += max(bridges[bridge][0], bridges[bridge+1][0] if bridge < n-1 else 0)
        bridge += 1
print(blocks)
        
