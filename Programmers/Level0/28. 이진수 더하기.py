# bin1 = "10", bin2 = "11", result = "101"
# bin1 = "1001", bin2 = "1111", result = "11000"

def solution(bin1, bin2):
    bin1 = int("0b" + bin1, 2) # 이진수로 만들기
    bin2 = int("0b" + bin2, 2)
    return bin(bin1 + bin2)[2:]