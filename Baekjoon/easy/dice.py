# https://www.acmicpc.net/problem/1233
a,b,c = map(int, input().split())
def dice(a,b,c):
    dic = {}
    for i in range(1, a+1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                add = i + j + k
                if add not in dic:
                    dic[add] = 1
                else:
                    dic[add] += 1

    # 첫번째 출력 방법
    maximum = 0
    for k, v in dic.items():
        if maximum < v:
            maximum = v
            answer = k
    print(answer)

    # # 두번째 출력 방법
    # answer2 = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    # print(answer2[0][0])

dice(a,b,c)
