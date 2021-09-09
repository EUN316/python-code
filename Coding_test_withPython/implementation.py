# 이것이 취업을 위한 코딩테스트다 with 파이썬
# CHAPTER 04. Implementation

# Example 4-1. 상하좌우
def exam_4_1():
    n = int(input("input N: "))
    directions = input("input Directions: ").split(' ') # 방향 계획서 list
    # 좌표 초기화
    x, y = 1, 1

    for direct in directions:
        if (direct == 'L') & (y > 1):
            y -= 1
        elif (direct == 'R') & (y < n):
            y += 1
        elif (direct == 'U') & (x > 1):
            x -= 1
        elif (direct == 'D') & (x < n):
            x += 1

    return x, y


# Example 4-2. 시각
def exam_4_2():
    n= int(input("input N: "))
    count = 0 # 3이 포함된 개수
    
    # 3중 for문
    for h in range(n+1): # n시까지
        for m in range(60): # 59분까지
            for s in range(60): # 59초까지
                if '3' in str(h)+str(m)+str(s):
                    count += 1

    return count


# Example 4-2. 왕실의 나이트
def exam_4_3():
    located = input("input Column-Row: ")
    row = int(located[1])
    col = ord(located[0])-ord('a')+1 # a=1부터 시작해서 얼만큼 떨어져 있는지

    # 모든 경로들의 이동 거리
    paths = [(-2,-1), (-2,1), (2, -1), (2,1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

    count = 0 # 경우의 수 초기화
    for path in paths:
        col_steped = col + path[0]
        row_steped = row + path[1]
        if (col_steped >= 1) & (col_steped <= 8) &(row_steped >= 1) & (row_steped <= 8):
            count += 1

    return count


# Example 4-3. 게임 개발
def exam_4_4():
    n, m = map(int, input("input N M: "))
    a, b, d = map(int, input("input A B d: ")) # 좌표(행, 열), 바라보는 방향
    ground = []
    for i in range(n):
        ground.append(map(int, input("input Map: ")))

    # 예시
    # n, m = 4, 4
    # a, b, d = 1, 1, 0
    # ground = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

    # 북, 동, 남, 서 idx에 왼쪽 회전하면 이동해야하는 step 넣어두기
    turned = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 현재 위치 방문 처리 -> 1로 변경 (바다랑 동일하게)
    ground[a][b] = 1
    count = 1 # 방문한 횟수

    flag = 0 # 네 방향 모두 막혀있는 경우를 확인하기 위해
    while True:
        # 왼쪽으로 회전
        d -= 1 
        if d == -1:
            d = 3
        
        # 왼쪽 방향으로 이동
        da = a + turned[d][0]
        db = b + turned[d][1]

        if (0 <= da) & (da < n) & (0 <= db) & (db < m): # 존재하는 곳일 때
            # 왼쪽 방향 칸이 가보지 않고 육지이면
            if ground[da][db] == 0: 
                ground[da][db] = 1 # 방문 처리
                a = da # 이동
                b = db # 이동
                flag = 0 # 초기화
                count += 1
            # 가봤거나 바다이면
            else: 
                flag += 1 # 본 방향 횟수

        # 네 방향이 다 막혀있으면,
        if flag == 4:
            da = a - turned[d][0] # 내 위치에서 반대로 이동하므로 - 처리
            db = b - turned[d][1]

            if (0 <= da) & (da < n) & (0 <= db) & (db < m): # 존재하는 곳일 때
                if ground[da][db] == 0: 
                    ground[da][db] = 1 # 방문 처리
                    a = da # 이동
                    b = db # 이동
                    flag = 0 # 초기화
                    count += 1
                else: # 갈 데가 더이상 없으면
                    break

    return count

        

if __name__ == "__main__":
    print("Implementation")
    print('exam_4_1: ', exam_4_1())
    print('exam_4_1: ', exam_4_2())
    print('exam_4_2: ', exam_4_3())
    print('exam_4_3: ', exam_4_4())