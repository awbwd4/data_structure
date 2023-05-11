products = [[20, 10], [10, 10], [15, 12], [25, 8], [20, 5]]

# products[i][1]//products[i][0]
remain = 30  # 배낭의 용량


def best_value_package(products, remain):
    # 1키로당 가치 기준으로 내림차순 재배열
    products.sort(key=lambda x: x[1] / x[0], reverse=True)
    print(products)

    value = 0

    for product in products:
        if remain < product[0]:
            value += (product[1] / product[0]) * remain
            remain = 0
            break
        else:
            remain -= product[0]
            value += product[1]

    return value


print(best_value_package(products=products, remain=remain))
