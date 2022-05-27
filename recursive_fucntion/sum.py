# sum = 0
def sum(n):
    print(n)
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    return sum(n - 1) + sum(n - 2) + sum(n - 3)


sum(5)
# print(sum(6))
