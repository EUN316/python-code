-- 동명 동물 수 찾기
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME