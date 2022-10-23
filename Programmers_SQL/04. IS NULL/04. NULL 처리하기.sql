SELECT ANIMAL_TYPE, IFNULL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- IFNULL의 의미
-- NAME의 이름이 null인 경우에는 'No name'으로 변환하기
-- AS 를 써서 컬럼명 변경해주기