SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
 IF(OUT_DATE <= '2022-05-01', '출고완료',
 IF(OUT_DATE IS NULL, '출고미정','출고대기')) AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;

-- 다른 방법
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
 (CASE WHEN DATEDIFF(OUT_DATE, '2022-05-01')<=0 THEN '출고완료'
 WHEN DATEDIFF(OUT_DATE, '222-05-01')>0 THEN '출고대기'
 ELSE '출고미정' END) AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;
