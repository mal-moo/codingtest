"""
    data structure: #map
    understand: y
    link: https://codeforces.com/problemset/problem/1426/D
"""

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * 200001
map = {}
answer = 0

map[0] = 1  # 수를 삽입해야하는 연속된 배열의 합이 0일 때를 확인하기 위한 초기화

for i in range(n):
    prefix_sum[i] = a[i]
    
    if i != 0:
        prefix_sum[i] += prefix_sum[i-1]

    if prefix_sum[i] in map:
        answer += 1
        map.clear()
        map[prefix_sum[i-1]] = 1  # 누적합부터 다시 수를 삽입해야 하는 연속의 배열의 합이 0일 때를 확인하기 위해 설정
    
    map[prefix_sum[i]] = 1

print(answer)
