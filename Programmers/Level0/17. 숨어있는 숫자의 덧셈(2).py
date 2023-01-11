# "aAb1B2cC34oOp" => 1 + 2 + 34 = 37 을 return
# "1a2b3c4d123Z" => 1 + 2 + 3 + 4 + 123 = 133 을 return
import re
def solution(my_string):
    arr = re.findall('\d+', my_string)
    return sum([int(i)for i in arr])

#re모듈 사용하기
print(re.findall('\d', '숫자123이 이렇게56 있다8')) # ['1', '2', '3', '5', '6', '8']
print(re.findall('\d+', '숫자123이 이렇게56 있다8')) # ['123', '56', '8']