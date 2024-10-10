WITH S AS (
    SELECT COUNT(*) AS t
    FROM ECOLI_DATA
)

SELECT E.ID, CASE WHEN E.r <= S.t / 4 THEN 'CRITICAL'
                WHEN E.r <= S.t / 2 THEN 'HIGH'
                WHEN E.r <= S.t * 3 / 4 THEN 'MEDIUM'
                ELSE 'LOW' END AS COLONY_NAME
FROM (
    SELECT ID, RANK() OVER (ORDER BY SIZE_OF_COLONY desc) AS r
    FROM ECOLI_DATA
) AS E, S
ORDER BY ID

