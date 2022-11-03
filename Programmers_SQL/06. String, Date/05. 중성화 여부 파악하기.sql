SELECT ANIMAL_ID, NAME, 
    CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
           OR SEX_UPON_INTAKE LIKE '%Spayed%' then 'O'
         ELSE 'X'
    END 중성화
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;

-- 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있음.
-- 동물의 아이디와 이름, 중성화 여부 조회: SELECT 이용
-- CASE WHENE ~ 중성화가 되어있을 때 'O', 
-- ELSE 아닐 때 'X'
-- END 뒤에 쓰는 말: 컬럼명
-- 아이디 순으로 조회 : ORDER BY 사용 