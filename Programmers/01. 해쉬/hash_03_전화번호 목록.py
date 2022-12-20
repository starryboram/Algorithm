# 처음 푼 코드 -> 테스트케이스 통과 -> 런타임 에러남(37.5점) 코드자체가 잘못된듯
def solution(phone_book):
    arr = [sorted(phone_book)[0]]
    new_arr = sorted(phone_book)[1:]
    for i in range(len(new_arr)-1):
        if arr[-1] in new_arr[i]:
            return False
        else:
            arr.append(i)
            new_arr.pop(0)
    return True

# 다시 푼 코드 -> 75점(시간초과남)
def solution(phone_book):
    new_arr = sorted(phone_book)
    for i in range(len(new_arr)-1):
        for j in range(len(new_arr[i+1:])):
            if new_arr[i] in new_arr[i+1:][j]:
                return False
    return True

# 코드 참고함
def solution(phone_book):
    new_arr = sorted(phone_book)
    for p1, p2 in zip(new_arr, new_arr[1:]):
        if p2.startswith(p1):
            return False
    return True

#startswith란 p1 글자가 p2에 앞에 있는지 검사함.
print("dwer2fagd".startswith("abcd"))  ### False
print("abcde14".startswith("abcd"))  ### True


# 정석풀이(Hash)★ 다시 한번 보자
def solution(phone_book):
    hash_map = {} # hashmap 생성
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True