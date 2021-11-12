"""
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

1 ≤ left ≤ right ≤ 1,000
"""
# 약수의 개수 계산 함수
def cal(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): # 제곱근까지만 확인
        if n%i == 0: # 약수이면
            cnt += 1
            if i**2 != n: # 제곱이 n이 아니면
                cnt += 1 
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        val = cal(i) # 약수 개수 반환 함수
        if val % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer