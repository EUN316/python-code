SELECT ROUND(LAT_N,4)
FROM (SELECT LAT_N, PERCENT_RANK() OVER (ORDER BY LAT_N) AS PERCENT
      FROM STATION) AS T1
WHERE PERCENT = 0.5