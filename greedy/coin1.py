coin_list = [1, 100, 50, 500]

coin_list.sort(reverse=True)

i: int = 0
total_count = 0
amount = 4720


while i < len(coin_list):
    count = 0
    if coin_list[i] <= amount:
        count = amount // coin_list[i]
        remain = amount % coin_list[i]
        total_count += count
        amount = remain
    else:
        i += 1


print(total_count)
