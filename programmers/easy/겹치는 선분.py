# 근혜님 방법
def solution(lines):
    dic = dict()
    for line in lines:
        for i in range(line[0], line[1]):
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
    cnt = 0
    for k,v in dic.items():
        if v > 1:
            cnt += 1
    return cnt

