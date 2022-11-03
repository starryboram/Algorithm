SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = "Lucy" or  NAME = "Ella" or  NAME = "Pickle"
or NAME = "Rogan" or NAME = "Sabrina" or NAME = "Mitty" 
ORDER BY ANIMAL_ID;

/* WHERE 부분 간단히 표현하기
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
만약 없는 동물 구할때는 IN 대신 NOT IN으로 바꿔쓰면 됨. */