n = 1260
count = 0


array = [500, 100, 50, 10]

for coin in array:
    print("coin : ", coin)
    print("n    : ", n)
    count += n // coin
    print("     count : ", count)
    n %= coin


print(count)


a = map(int, input().split())
