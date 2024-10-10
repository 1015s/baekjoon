WITH RECURSIVE r AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT e.ID, e.PARENT_ID, r.GENERATION + 1 AS GENERATION
    FROM ECOLI_DATA AS e JOIN r ON e.PARENT_ID = r.ID
), c AS (
    SELECT M.ID AS ID, COUNT(M.ID) AS cnt
    FROM ECOLI_DATA M JOIN ECOLI_DATA S
    ON M.ID = S.PARENT_ID
    GROUP BY M.ID
)

SELECT COUNT(*) AS COUNT, r.GENERATION
FROM r LEFT JOIN c ON r.ID = c.ID
WHERE c.cnt IS NULL
GROUP BY r.GENERATION