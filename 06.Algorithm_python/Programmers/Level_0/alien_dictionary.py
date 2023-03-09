# https://school.programmers.co.kr/learn/courses/30/lessons/120869
def solution(spell, dic):
    spell = ''.join(sorted(spell))
    for word in dic:
        word = ''.join(sorted(word))
        if word == spell:
            return 1
    return 2

# best
def solution(spell, dic):
    for word in dic:
        if not set(spell) - set(word):
            return 1
    return 2