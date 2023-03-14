# https://school.programmers.co.kr/learn/courses/30/lessons/120883?language=python3
def solution(id_pw, db):
    for array in db:
        if id_pw[0] == array[0]:
            if id_pw[1] == array[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'

# best
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return 'login' if db_pw == id_pw[1] else 'wrong pw'
    return 'fail'