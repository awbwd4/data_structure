test_case = int(input())


for _ in range(test_case):
    string = input()
    stackA = []
    stackB = []
    for i in range(len(string)):
        if string[i] == "<":
            if stackA:
                stackB.append(stackA.pop())
        elif string[i] == ">":
            if stackB:
                stackA.append(stackB.pop())
        elif string[i] == "-":
            if stackA:
                stackA.pop()
        else:
            stackA.append(string[i])
    stackA.extend(stackB)


print("".join(stackA))
