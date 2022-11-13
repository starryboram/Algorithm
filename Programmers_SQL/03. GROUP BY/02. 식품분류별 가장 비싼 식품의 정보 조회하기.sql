-- 처음 푼 방식
SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC;

-- 잘못된 결과 초래: CATEGORY와 MAX_PRICE값은 제대로나오지만, PRODUCT_NAME이 잘 못 나옴
-- PRODUCT_NAME까지 조건이 걸리지 않음 -> 서브쿼리 사용 해야함


-- 다음에 푼 방식
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
AND CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;

-- FOOD_PRODUCT 테이블 : FROM FOOD_PRODUCT
-- 식품분류별로 가격이 제일 비싼 식품 조회: SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
-- 분류, 가격, 이름을 조회: SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력: AND CATEGORY IN ('과자', '국', '김치', '식용유')
-- 식품 가격을 기준으로 내림차순 정렬: ORDER BY MAX_PRICE DESC
-- ※ 각 행별로 최대 가격을 봐야함 => WHERE 구문에 서브쿼리 이용해서 집어넣기