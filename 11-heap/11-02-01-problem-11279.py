"""
    data structure: #priority_queue
    understand: n
    link: https://www.acmicpc.net/problem/11279
"""

import sys
import heapq  # 우선순위 큐를 위한 라이브러리

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num != 0:
        heapq.heappush(heap, (-num))  # heapq가 최소힙 기준으로 만들어져서 최대힙을 이용시 음수화 처리를 한다.
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
