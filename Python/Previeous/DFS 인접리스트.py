# 인접 리스트
# 갈수있는 지점만 저장
# 주의사항 - 각 노드마다 갈수있는 지점의 개수가 다름
# range 쓸때 index 조심
# 메모리적으로 인접행렬에비해 훨씬 효율적이다
graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]
# 파이썬은 딕셔너리로도 구현할 수 있음

# graph = {
#    '0': [1,3],
#    '1': [0,2,3,4],
#    '2': [1],
#    '3': [0,1,4],
#    '4': [1,3]
# }

# make_star
# stack 버전
def make_star_stack(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        #방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 작은번호부터 조회 하고 싶다면
        for to in range(len(graph[now]) - 1, -1, -1):
            # 이제 연결이 안되어있다는건 애초에 저장하지 않았으므로 체크할 필요 없음
            # 방문한 지점이라면 stack에 추가하지 않음
            next = graph[now][to]
            # 인접리스트를 쓸때는 인덱스와 값이 다를수가 있으므로 값을 지정해주어야한다
            if next in visited:
                continue

            stack.append(next)
    return visited
print("make_star stack = ", end= '')
print(*make_star_stack(0))
# 재귀
# map 크기, 길이를 알때 append 형식 말고 아래와 같이 사용하면 빠르다
visited = [0]*5
path = [] # 방문 순서 기록

def make_star(now):
    visited[now] = 1 # 현재지점 방문 표시
    #print(now, end=' ')
    path.append(now)
    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        next = graph[now][to]
        if visited[next]:
            continue
        make_star(next)

print('make_star 재귀 =', end=' ')
make_star(0)
print(path)
