data_list = [(10, 10), (15, 12), (25, 8), (30, 5), (20, 10)]


print(data_list)


def get_max_value(data_list, capacity):
    # capacity : 가방의 무게 제한

    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    # 무게 대비 가치가 높은 것 부터 차례로 소팅

    total_value = 0
    detail = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            detail.append([data[0], data[1], 1])  # 무게, 가치, 비율
        else:
            # 현재 가치를 넣기에 부족하다면?
            # 쪼개서 넣는다
            # 몇 퍼센트를 넣을지를 계산해야함.
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            detail.append([data[0], data[1], fraction])  # 무게, 가치, 비율
            break  # 다음 물건들은 더 이상 볼 필요가 없음.
    return total_value, detail


print(get_max_value(data_list, 30))
