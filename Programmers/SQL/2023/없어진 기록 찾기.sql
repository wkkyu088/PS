SELECT T2.ANIMAL_ID, T2.NAME
FROM ANIMAL_INS AS T1
RIGHT OUTER JOIN ANIMAL_OUTS AS T2 ON T1.ANIMAL_ID = T2.ANIMAL_ID
WHERE T1.DATETIME IS NULL
ORDER BY T1.ANIMAL_ID