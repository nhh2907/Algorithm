# https://school.programmers.co.kr/learn/courses/30/lessons/120843
def solution(numbers, K):
    n = len(numbers)      # 배열의 길이
    i = 0                 # 현재 공을 가진 사람의 인덱스
    for _ in range(K-1):  # K번 반복
        i = (i + 2) % n   # 공을 던질 대상의 인덱스
    return numbers[i]     # K번째로 공을 던지는 사람의 번호 리턴

# Best 
def solution(numbers, K):
    return numbers[(K - 1) * 2 % len(numbers)] # 2를 K-1번 곱하고 총 개수로 나눔