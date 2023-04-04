# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    total = sum([int(i) for i in str(x)])
    if not x%total:
        return True
    else:
        return False

# best
def solution(x):
    return x%sum([int(i) for i in str(x)]) == 0