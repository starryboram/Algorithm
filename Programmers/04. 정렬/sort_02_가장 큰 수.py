def solution(numbers):
    nubmers = list(map(str, numbers)) # numbers에 있는 원소를 string 형태로 만들어서 list로 담아준다.
    numbers.sort(key = lambda x:*3, reverse = True) #numbers 원소를 똑같이 3번을 씀 => 3을 333으로 만듦
    return str(int(''.join(numbers)))