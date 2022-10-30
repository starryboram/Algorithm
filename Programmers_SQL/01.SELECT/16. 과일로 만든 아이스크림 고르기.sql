SELECT a.FLAVOR
FROM FIRST_HALF AS a
INNER JOIN ICECREAM_INFO AS b
ON a.FLAVOR = b.FLAVOR
WHERE TOTAL_ORDER > 3000
AND b.INGREDIENT_TYPE = 'fruit_based';

-- 총 주문량이 3000이상인 애들을 조회: WHERE 조건절 이용 
-- 1개의 테이블로 추정하기 힘듦: JOIN 사용하기