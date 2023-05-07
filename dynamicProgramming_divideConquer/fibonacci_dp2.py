n = int(input())


def fib_dp(num):
    cache = [0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2,num+1):
        cache[i] = cache[i-1]+cache[i-2]

    return cache[num]

print(fib_dp(n))