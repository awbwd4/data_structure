n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

# 2 3 3      3 4 4 5 5       5
# 1             1
for i in data:  # 공포도를 낮은것 부터 하나씩 확인.
    count += 1  # 현재 그룹에 해당 모헙가를 포함시키기.
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재 지정된 모험가의 공포도 이상이라면
        count = 0  # 모험가의 수 초기화
        result += 1  # 그룹의 수 1 증가


print(result)
