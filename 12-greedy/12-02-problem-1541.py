"""
    data structure: #greedy
    understand: y
    link: https://www.acmicpc.net/problem/1541
"""
equation = input().split('-')
answer = 0

for i in equation[0].split('+'):
    answer += int(i)

for i in equation[1:]:
    for j in i.split('+'):
        answer -= int(j) 

print(answer)
