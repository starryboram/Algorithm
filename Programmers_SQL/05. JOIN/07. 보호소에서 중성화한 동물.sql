SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
ORDER BY A.ANIMAL_ID;

-- 보호소에 들어올 당시에는 중성화되지 않았다: (Intake살피기)
-- 보호소를 나갈 당시에는 중성화된 동물: (outcome 살피기)
-- 아이디와 생물 종, 이름을 조회: SELECT ANIMAL_ID, TYPE, NAME
-- 아이디 순으로 조회: ORDER BY ANIMAL_ID
-- 한마디로 INS와 비교했을때 OUTS에서 값이 변경된 애들 찾기: WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME