# n = int(input) # 줄에 서있는 사람의 수
# p = list() # 각 사람이 돈을 인출하는데 걸리는 시간

# for i in range(n):
#     p.append(int(input()))


def min_wait_time(p):
    p.sort()
    print(p)

    total_time = 0  # 필요한 시간의 합을 저장

    for i in range(len(p)):
        a = p[: i + 1]
        total_time += sum(p[: i + 1])
        print(f"{i} = {total_time}, p[:i+1] = {a}")

    return total_time


array = [3, 1, 4, 3, 2]


print(min_wait_time(p=array))
