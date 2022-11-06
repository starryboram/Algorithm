SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

/*  참고

"2022-04-11"을 date_format 시키면
%Y : 2022 로 출력          %y : 22 로 출력
%M : April로 출력          %m : 04 로 출력
%D : 11th 로 출력          %d : 11 로 출력

*/