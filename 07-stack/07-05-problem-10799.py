"""
    data structure: #stack
    understand: y
    link: https://www.acmicpc.net/problem/10799
"""

brackets = input()

stack = []
answer = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        if brackets[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)