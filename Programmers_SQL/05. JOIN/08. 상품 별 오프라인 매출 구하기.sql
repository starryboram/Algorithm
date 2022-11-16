SELECT P.PRODUCT_CODE, (SUM(O.SALES_AMOUNT) * P.PRICE) AS SALES
FROM PRODUCT AS P
INNER JOIN OFFLINE_SALE AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;

-- PRODUCT 테이블과 OFFLINE_SALE 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력
-- 매출액을 기준으로 내림차순 정렬
-- 매출액이 같다면 상품코드를 기준으로 오름차순 정렬