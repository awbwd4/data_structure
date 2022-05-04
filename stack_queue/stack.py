stack = []  ##파이썬에서 스택은 별 다른 라이브러리 필요 없이 리스트로 구현이 가능함.


# 5, 2, 3, 7, 삭제, 1, 4, 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  ## 선입부터 출력해줌
print(stack[::-1])  ##후입부터 출력
