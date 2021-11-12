-- 보호소에서 중성화한 동물
SELECT T1.ANIMAL_ID, T1.ANIMAL_TYPE, T1.NAME
FROM ANIMAL_INS AS T1
INNER JOIN ANIMAL_OUTS AS T2 ON T1.ANIMAL_ID = T2.ANIMAL_ID
WHERE T1.SEX_UPON_INTAKE LIKE 'Intact%' 
AND (T2.SEX_UPON_OUTCOME LIKE 'Spayed%' OR T2.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY T1.ANIMAL_ID