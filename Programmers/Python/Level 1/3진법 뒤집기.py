"""
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

n은 1 이상 100,000,000 이하인 자연수입니다.
"""
def solution(n):
    answer = 0
    # 10진수 -> reverse 3진수
    rev = ''
    while True:
        if n == 0: break
        rev = str(n%3) + rev
        n = n//3
        
    # 3진수 reverse -> 10진수
    for i in range(len(rev)):
        if i == 0:
            answer += int(rev[i])
        else:
            answer += (3**i)*int(rev[i])
        
    return answer