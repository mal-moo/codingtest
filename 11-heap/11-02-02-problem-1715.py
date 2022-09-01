"""
    data structure: #priority_queue
    understand: y
    link: https://www.acmicpc.net/problem/1715
"""
import heapq

n = int(input())
cards = list(int(input()) for _ in range(n))

heapq.heapify(cards)
answer = 0

while len(cards) != 1:
    print('cards: ', cards)
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    sum = first + second
    answer += sum 
    heapq.heappush(cards, sum) 

print(answer)

