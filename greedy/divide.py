n = 7
k = 3

print(type(n))
print(type(k))

while n >= k:
    if n % k == 0:
        n //= k
    else:
        n - 1
    print(n)
