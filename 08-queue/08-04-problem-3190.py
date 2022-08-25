"""
    data structure: #queue
    understand: y
    link: https://www.acmicpc.net/problem/3190
    memo: direction_change() 수식 기억하기

"""
from collections import deque


def direction_change(direction, c):
    if c == 'L':
        direction = (direction-1) % 4  # 반시계방향으로 회전 (상(0)->우(1)->하(2)->좌(3)->상(0))
    else:
        direction = (direction+1) % 4  # 시계방향으로 회전 (상(0)->좌(3)->하(2)->우(1)->상(0))
    
    return direction


N = int(input())
K = int(input())
board = [[0]* N for _ in range(N)]  # 2차원 배열 만들기
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1  # 사과 위치 저장하기

L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C  # 방향 변화 저장하기

# 방향키
# direction 0: 상, 1: 우, 2: 하, 3: 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1  # 처음엔 무조건 오른쪽으로 이동하므로 1로 시작
time = 1
x, y = 0, 0  # 뱀 처음 위치
snake = deque([(x, y)])
board[x][y] = 2  # 뱀이 위치하는 곳은 2 값을 가짐

while True:
    x, y = x + dx[direction], y + dy[direction]
    
    if 0 <= x < N and 0 <= y < N and board[x][y] != 2:  # 벽 또는 자기 자신을 마주치면 게임 끝
        if board[x][y] != 1:  # 이동한 곳에 사과가 없을 경우
            del_x, del_y = snake.popleft()  # 뱀 꼬리 제거
            board[del_x][del_y] = 0
        board[x][y] = 2  # 이동한 곳에 뱀의 위치값 2 저장
        snake.append([x, y])  # 뱀 위치값 저장

        if time in times.keys():  # 방향 변경된 시간이라면
            direction = direction_change(direction, times[time])

        time += 1
    else:
        break

print(time)
