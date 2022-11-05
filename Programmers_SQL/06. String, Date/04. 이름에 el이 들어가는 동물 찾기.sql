SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = "Dog"
AND NAME LIKE "%EL%"
ORDER BY NAME;

-- 'EL'이 들어가는 개 찾기: where구문 활용하기
-- 개의 아이디와 이름을 조회: SELECT 
-- 이름 순으로 조회: ORDER BY NAME
