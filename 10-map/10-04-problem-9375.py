"""
    data structure: #map
    understand: y
    link: https://www.acmicpc.net/problem/9375
"""

testcases = int(input())

for i in range(testcases):
    map = {}
    answer = 1
    n = int(input())
    
    for j in range(n):
        a, b = input().split()
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1
    
    for k in map:
        answer *= map[k] + 1

    print(answer-1)
