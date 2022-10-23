SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;

-- IFNULL ~만 사용할 경우에는 해당 이름이 컬럼명으로 변경됨 -> AS를 사용하여 컬럼명 변경하기
-- 경기도에 위치한 애들만 뽑아내고 싶음 -> WEHRE ~~ LIKE를 이용하여 문자열 검색하기