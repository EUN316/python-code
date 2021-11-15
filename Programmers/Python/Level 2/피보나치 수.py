"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

n은 2 이상 100,000 이하인 자연수입니다.
"""
def func_fibo(n):
    fibo = [0,1] # 피보나치 수열 저장 리스트
    for i in range(2, n+1): # 2 ~ n까지 연산
        fibo.append(fibo[i-1] + fibo[i-2]) # i번째 수열 계산하여 추가
    
    return fibo[n]

def solution(n):
    answer = func_fibo(n)
    
    return answer % 1234567