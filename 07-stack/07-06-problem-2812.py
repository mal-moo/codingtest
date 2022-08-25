"""
    data structure: #stack
    understand: y
    link: https://www.acmicpc.net/problem/2812
"""
n, k = map(int,input().split())
numbers = list(input())

answer = []
cnt = k

for num in numbers:
    while answer and cnt > 0 and answer[-1] < num:
        answer.pop()
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))