"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
"""
def solution(s):
    answer = ''
    flag = 0
    for t in s:
        if flag%2 == 0: # 짝수 idx
            t = t.upper()
        elif flag%2 != 0: # 홀수 idx
            t = t.lower()
        answer += t
        flag += 1
        if t == ' ': # 공백이면
            flag = 0 # idx 초기화
            
    return answer