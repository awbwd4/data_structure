from typing import List

coin_list = [1, 100, 50, 500]


def min_coin_count(value, coin_list: List):
    total_coin_cnt = 0
    detail = list()
    coin_list.sort(reverse=True)
    print(coin_list)

    for coin in coin_list:
        coin_count = value // coin
        total_coin_cnt += coin_count

        value -= coin * coin_count
        detail.append([coin, coin_count])
    return total_coin_cnt, detail


print(min_coin_count(4720, coin_list))
