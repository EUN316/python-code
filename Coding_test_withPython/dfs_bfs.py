# 이것이 취업을 위한 코딩테스트다 with 파이썬
# CHAPTER 05. DFS/BFS

# Example 5-1. 스택
def func_stack():
    stack = [] # 리스트로 스택 생성

    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    print(stack) # 최하단에 있는 경우부터 출력
    print(stack[::-1]) # 최상단 원소부터 출력 -> 끝까지 pop을 했을 경우와 동일


# Example 5-2. 큐
from collections import deque
def func_queue():
    queue = deque() # 라이브러리를 사용하여 큐 생성

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft() # 왼쪽부터(=먼저 들어온 애부터) 반환
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue) # 먼저 들어온 순서대로 출력 (FIFO)
    queue.reverse() # 역순
    print(queue) # 가장 나중에 들어온 경우부터 출력


# Example 5-3. 팩토리얼 재귀함수
def factorial_recursive(n): # n!
    if n <= 1: # 1이 되면 1을 반환
        return 1

    return n * factorial_recursive(n-1) # n! = n * (n-1)


# Example 5-8. DFS
def dfs(graph, v, visited): # graph: 그래프, v: 해당 노드 idx, visited: 방문 여부
    visited[v] = True # 방문처리
    print(v, end=' ') # 출력

    for i in graph[v]: # 인접 노드들을 방문
        if not visited[i]: # 방문하지 않았으면 False
            dfs(graph, i, visited) # 재귀함수 호출


from collections import deque
# Example 5-8. BFS
def bfs(graph, start, visited): # started: 시작 노드
    queue = deque([start])  # queue에 추가
    visited[start] = True # 방문처리

    while queue: # 빈 큐가 될 때까지
        v = queue.popleft() # 노드 하나 추출
        print(v, end=' ') # 출력
        
        for i in graph[v]: # 인접 노드들을 방문
            if not visited[i]: # 방문하지 않았으면 False
                queue.append(i) # 큐에 추가
                visited[i] = True # 방문처리


# Example 5-10. 음료수 얼려 먹기
def exam_5_10():
    n, m = map(int, input("input N M: ").split(' '))
    

    return


if __name__ == "__main__":
    # print('BFS/DFS')
    # print('func_stack: ', func_stack())
    # print('func_queue: ', func_queue())
    # print('factorial_recursive: ', factorial_recursive(5))
    graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
    visited = [False] * 9
    print('dfs: ')
    dfs(graph, 1, visited)
    print('')
    visited = [False] * 9
    print('bfs: ')
    bfs(graph, 1, visited)
    print('')

