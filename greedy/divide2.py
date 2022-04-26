n, k = map(int, input().split())

print(n, k)

result = 0


while True:
    # N이 K로 나누어 떨어지는 수가 될때까지 나누기
    target = (n // k) * k  # n이 k로 나눠 떨어지지 않을때, n에서 가장 가까운 k의 배수
    result += n - target
    # n이 k의 배수가 되기 위해서 1을 빼야 하는 횟수임
    # 예를들면 n == 107, k == 10, target == 100인 경우
    # n은 1을 7번을 빼야 k의 배수가 된다
    # 그 7번 == n - target임
    n = target
    # N이 k보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    result += 1
    n //= k

result += n - 1
# 나눗셈을 반복하기 때문에 어차피 n에서 나올 수 있는 가장 작은 값은 1임.
# 위의 계산 마지막 값이 1인 경우에는 추가로 -1을 해야할 연산 횟수가 0
print(result)

# 실제로 연산을 하는것이 아니라 횟수를 구하는것!!! 결국 횟수만 구하면 되는 일임.
