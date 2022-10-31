SELECT extract(hour from datetime) HOUR, count(*) COUNT
FROM ANIMAL_OUTS
where extract(hour from datetime) >=9 
and extract(hour from datetime) < 20
group by 1
order by 1;

-- extract의 경우에는 특정 날짜/시간 영역을 추출하여 출력하는 함수
-- 문제에서 9:00 ~ 19:59까지의 입양 건수를 보고싶어함 -> 시간대별 count 필요 (select에 씀)