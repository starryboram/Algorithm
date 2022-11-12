-- 0시부터 23시까지: WHERE @HOUR < 23
-- 각 시간대별 입양 발생 건수 조회: DATETIME 사용해서 COUNT 쓰기
-- 시간대 순으로 정렬: ORDER BY 굳이 안써도 됨.

-- 방법 1
SET @HOUR = -1;
SELECT (@HOUR:= @HOUR +1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME))
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME)=@HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR<23;

-- 방법 2
(select count(ao2.animal_id) from animal_outs ao2 where date_format(ao2.datetime, '%H') = @hour ) as cnt