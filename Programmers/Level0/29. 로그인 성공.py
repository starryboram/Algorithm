def solution(id_pw, db):
    while True:
        arr = []
        for i in db:
            if (id_pw[0] == i[0]) and (id_pw[1] == i[1]):
                arr.append("login")
            elif (id_pw[0] == i[0]) and (id_pw[1] != i[1]):
                arr.append("wrong pw")
            else:
                arr.append("fail")
        if "login" in arr:
            return "login"
        elif "wrong pw" in arr:
            return "wrong pw"
        else:
            return "fail"

# 간편 풀이
def solution(id_pw, db):
    dic = dict(db)
    if dic.get(id_pw[0],-1) == id_pw[1]:
        return "login"
    elif dic.get(id_pw[0],-1) == -1:
        return "fail"
    else:
        return "wrong pw"


# 다른풀이
def solution(id_pw, db):
    ID,PW = id_pw
    db_dict = {}
    for i,p in db:
        db_dict[i] = p
    if ID in db_dict:
        if db_dict[ID]==PW:
            return 'login'
        return 'wrong pw'            
    return 'fail'
