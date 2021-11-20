"""
DFS/BFS

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
"""
def bfs(n, computers, com, visit):
    visit[com] = True # 방문처리
    queue = [com] # com을 넣은 큐 생성
    
    while len(queue) != 0: # 큐가 비어있지 않을 때까지
        com = queue.pop()
        visit[com] = True # 방문처리
        for neighbor in range(n):
            if neighbor != com and computers[com][neighbor] == 1: # 자기 자신이 아니면서 네트워크 연결이 되어 있으면
                if visit[neighbor] == False: # 아직 이웃 방문처리가 안되어있으면
                    queue.append(neighbor) # 큐에 추가

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)] # 방문여부 리스트
    
    for com in range(n):
        if visit[com] == False: # 아직 방문하지 않았으면
            bfs(n, computers, com, visit) # BFS 진행
            answer += 1 # 네트워크 하나 추가
    
    return answer