SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
WHERE A.ANIMAL_ID NOT IN
        (SELECT B.ANIMAL_ID
         FROM ANIMAL_OUTS B)
ORDER BY A.DATETIME
LIMIT 3;
-- 아직 입양을 못 간 동물 중 -> NOT IN 쓰기
-- 가장 오래 보호소에 있었던 동물 3마리 구하기 -> LIMIT 쓰기
-- 이름과 보호 시작일을 조회 -> SELECT NAME, DATETIME
-- 보호 시작일 순으로 조회 -> ORDER BY DATETIME

