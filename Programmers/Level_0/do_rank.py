# https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    avg_sorted = sorted([(a+b)/2 for a, b in score], reverse=True)
    
    dic = {}
    i = 1
    for num in avg_sorted:
        if num in dic: 
            i += 1
        else :
            dic[num] = i
            i += 1
    
    return [dic[(a+b)/2] for a, b in score]

# best_1
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

# best_2
def solution(score):
    rank = sorted([sum(i) for i in score], reverse=True)
    rank_dict = {}
    for i, num in enumerate(rank):
        if num not in rank_dict:
            rank_dict[num] = i+1
    return [rank_dict[sum(i)] for i in score]

