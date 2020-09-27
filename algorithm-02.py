n = int(input())
teas = list(map(float, input().split()))
f = [0] * n
f[1] = teas[0] + teas[1]
f[2] = teas[1] + teas[2]
f[3] = teas[0] + teas[2] + teas[3]
f[4] = teas[0] + teas[1] + teas[3] + teas[4]
for i in range(5, n):
    f[i] = max(
            f[i-3] + teas[i-1] + teas[i],
            f[i-4] + teas[i-1] + teas[i],
            f[i-5] + teas[i-3] + teas[i-1] + teas[i]
        )
print(max(f[n-1], f[n-2], f[n-3] + teas[n-1]))
'''
def f(x):
    if x <= 0:
        return 0
    if x == 1:
        return teas[0] + teas[1]
    if x == 2:
        return teas[1] + teas[2]
    if x == 3:
        return teas[0] + teas[2] + teas[3]
    return max(f(x-3) + teas[x-1] + teas[x], f(x-4) + teas[x-1] + teas[x],\
               f(x-5) + teas[x-3] + teas[x-1] + teas[x])

print(max(f(n-1), f(n-2), f(n-3) + teas[n-1]))
'''
