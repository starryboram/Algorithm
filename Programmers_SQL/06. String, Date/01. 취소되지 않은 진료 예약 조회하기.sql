SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO
JOIN DOCTOR D ON A.MCDP_CD = D.MCDP_CD AND A.MDDR_ID = D.DR_ID
WHERE (A.APNT_YMD BETWEEN "2022-04-13 00:00:00" AND "2022-04-13 23:59:59")
AND (A.MCDP_CD = "CS")
AND (A.APNT_CNCL_YN = "N")
ORDER BY A.APNT_YMD

 -- where 구문을 똑똑하게 쓰는 방법
 -- 2022년 4월 13일 날짜 출력하기: WHERE TO_CHAR(a.apnt_ymd, 'YYYY-MM-DD') = '2022-04-13'