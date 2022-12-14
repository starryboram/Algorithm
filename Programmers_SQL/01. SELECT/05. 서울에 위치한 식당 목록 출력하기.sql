SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO AS I
JOIN REST_REVIEW AS R
ON I.REST_ID = R.REST_ID
WHERE ADDRESS LIKE '서울시%' OR ADDRESS LIKE '서울특별시%'
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;

-- REST_INFO와 REST_REVIEW 테이블에서
-- : FROM REST_INFO AS I
-- JOIN REST_REVIEW AS R
-- ON I.REST_ID = R.REST_ID 

-- 서울에 위치한 식당들의: WHERE ADDRESS LIKE '서울시%' OR ADDRESS LIKE '서울특별시%'

-- 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회
-- : SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS,

-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림: ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE

-- 평균점수 기준 내림차순 정렬 / 평균점수 같을 경우 즐겨찾기수를 기준 내림차순 정렬
-- : WHERE ADDRESS LIKE '서울시%' OR ADDRESS LIKE '서울특별시%'