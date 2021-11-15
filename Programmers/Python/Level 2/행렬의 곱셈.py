"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""
def solution(arr1, arr2):
    # 행렬 곱: 행렬1의 row과 행렬2의 col의 각 원소의 곱의 누적합
    answer = [[sum(a * b for a, b in zip(row_1, col_2)) # arr1 row * arr2 col 원소의 곱의 누적합
               for col_2 in zip(*arr2)] # arr2의 각 colum
              for row_1 in arr1] # arr1의 각 row
    return answer
