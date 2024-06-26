import sys
sys.stdin = open('input.txt')

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(sti, stj, N):
    queue = []
    visited = [[0]*(N) for _ in range(N)]
    queue.append((sti, stj))
    visited[sti][stj] = 1
    while queue:
        i, j = queue.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]-2 # 지나온 칸 수 리턴
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착점에 도달할 수 없는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc}', ans)