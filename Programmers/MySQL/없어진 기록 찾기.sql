-- 없어진 기록 찾기
SELECT T1.ANIMAL_ID, T1.NAME
FROM ANIMAL_OUTS AS T1
LEFT JOIN ANIMAL_INS AS T2 ON T1.ANIMAL_ID = T2.ANIMAL_ID
WHERE T2.DATETIME IS NULL
ORDER BY T1.ANIMAL_ID