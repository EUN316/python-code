"""
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

n은 1이상, 50000000000000 이하인 양의 정수입니다.
"""
import math

def solution(n):
    answer = 0
    
    x = int(math.sqrt(n)) # int(sqrt)에서 시작
    while x > 0:
        if x**2 == n: # n이 x의 제곱이면
            answer = (x+1)**2
            break
        x -= 1 
        
    if x == 0: # 0이면
        answer = -1
    
    return answer