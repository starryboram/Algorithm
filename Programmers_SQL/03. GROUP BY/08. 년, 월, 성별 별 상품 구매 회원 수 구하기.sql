SELECT YEAR(B.SALES_DATE) AS YEAR, 
		MONTH(B.SALES_DATE) AS MONTH,
        A.GENDER AS GENDER, 
        COUNT(DISTINCT A.USER_ID) AS USERS
FROM USER_INFO A 
JOIN ONLINE_SALE B 
ON A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH, GENDER
HAVING GENDER IS NOT NULL 
ORDER BY YEAR, MONTH, GENDER;

-- YEAR, MONTH, GENDER 골라낼 때 SALES_DATE TYPE이 DATE이기 때문에 YEAR로 바로 골라내도 괜찮다.
-- USER_ID 중복 제거를 해줘야하며, JOIN문을 이용하여 두 테이블을 합쳐서 결과를 도출하면 된다.
-- GROUP BY를 이용해서 묶고 난 후에, 조건문을 활용(HAVING) 해서 결과를 빼낸다.
-- 이 문제는 블로그를 참고하여 풀었다.