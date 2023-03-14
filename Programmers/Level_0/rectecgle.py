# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    a = [x for x, y in dots]
    b = [y for x, y in dots]
    return (max(a)-min(a)) * (max(b)-min(b))

# best
def solution(dots):
    a = sorted([x for x, y in dots])
    b = sorted([y for x, y in dots])
    return (a[-1]-a[0]) * (b[-1]-b[0])

# best
def solution(dots):
    return (max(dots)[0]-min(dots)[0]) * (max(dots)[1]-min(dots)[1])