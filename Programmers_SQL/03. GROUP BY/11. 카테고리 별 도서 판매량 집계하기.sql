SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK
JOIN BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE DATE(SALES_DATE) BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY CATEGORY
ORDER BY CATEGORY