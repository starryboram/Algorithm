SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = "Dog"
AND NAME LIKE "%EL%"
ORDER BY NAME;

-- 할머니가 기르던 '개' : ANIMAL_TYPE = "Dog"
-- 개는 이름에 'el'이 들어감 : "&EL%"
-- 이름 순으로 조회 : ORDER BY NAME