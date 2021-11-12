"""
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

x는 1 이상, 10000 이하인 정수입니다.
"""
def solution(x):
    answer = True # 하샤드 수 여부
    x_sum = sum(map(int, str(x))) # 각 자리 수의 합 계산
    if x % x_sum != 0: # 자릿수의 합으로 나누어 떨어지지 않으면
        answer = False
    return answer