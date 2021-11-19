"""
완전탐색 

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
"""
def solution(brown, yellow):
    answer = [] # 가로(w), 세로(h)
    wh = brown + yellow # 전체 격자 개수
    for i in range(3, wh): # 한 변의 길이가 무조건 3보다 길어야 함
        if wh % i == 0: # 약수이면
            if (i - 2) * (wh//i - 2) == yellow:
                answer = [i, wh//i]
                break
                
    answer.sort(reverse = True) # 가로 > 세로            
    return answer

# def solution(brown, yellow):
#     answer = [] # 가로, 세로
#     wh = brown + yellow
#     for i in range(1,wh):
#         if wh%i==0:
#             w, h = wh//i, i
#             if (w-2)*(h-2) == yellow and 2*(w+h)-4 == brown:
#                 return [w, h]
#     return answer