# "onetwothreefourfivesixseveneightnine" -> 123456789로 나오게 해주세요.

def solution(numbers):
    return int(numbers.replace('one','1').replace('two','2').replace('three','3')
    .replace('four','4').replace('five','5').replace('six','6').replace('seven','7')
    .replace('eight','8').replace('nine','9').replace('zero','0'))

# 다른 사람의 풀이1
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

# 다른 사람의 풀이2
def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)

# 다른 사람의 풀이3
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)