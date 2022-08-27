"""
    data structure: #arraylist
    understand: y
    link: https://www.acmicpc.net/problem/10818
"""

n = int(input())
array_list = list(map(int, input().split()))

# (1)
# max_num = array_list[0]
# min_num = array_list[0]

# for num in array_list:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# (2)
max_num = max(array_list)
min_num = min(array_list)

print(min_num, max_num)