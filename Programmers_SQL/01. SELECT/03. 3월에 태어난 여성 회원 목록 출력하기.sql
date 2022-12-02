SELECT MEMBER_ID, MEMBER_NAME,GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH 
FROM MEMBER_PROFILE
WHERE TLNO IS NOT NULL 
AND GENDER = 'W'
AND DATE_FORMAT(DATE_OF_BIRTH,'%m') = '03'
ORDER BY MEMBER_ID;

-- DATE_FORMAT을 통해 원하는 날짜형식으로 변경이 가능하다. 이때, 컬럼명이 바뀌니까 AS를 써서 바꿔줌.
-- 전화번호가 NULL인 경우 제외해주세요 -> IS NOT NULL로 사용하기
-- 여성 회원 출력 -> GENDER = 'W'
-- 3월 회원 -> DATE_FORMAT함수 이용해서 '%m' == 3인 애들만 추출하기
-- 회원ID 기준으로 오름차순 정렬하기(DEFAULT가 오름차순이기 때문에 굳이 뒤에 안붙임)