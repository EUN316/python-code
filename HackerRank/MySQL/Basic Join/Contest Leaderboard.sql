SELECT H.hacker_id, H.name, T2.total_score
FROM (SELECT T1.hacker_id, SUM(max_score) AS total_score
      FROM (SELECT hacker_id, challenge_id, MAX(score) AS max_score
            FROM Submissions
            GROUP BY hacker_id, challenge_id) T1
      GROUP BY T1.hacker_id
      HAVING total_score != 0) T2
INNER JOIN Hackers H ON H.hacker_id = T2.hacker_id
ORDER BY T2.total_score DESC, H.hacker_id ASC