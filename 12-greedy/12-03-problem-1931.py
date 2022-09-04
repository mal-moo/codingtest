"""
    data structure: #greedy
    understand: y
    link: https://www.acmicpc.net/problem/1931
"""
N = int(input())
meet = []

for i in range(N):
    A, B = map(int, input().split())

    meet.append([A, B])

meet.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = 0

for i in range(len(meet)):
    if end_time <= meet[i][0]:
        end_time = meet[i][1]
        answer += 1

print(answer)
