SELECT *
FROM (
		SELECT MCDP_CD AS "진료과코드", COUNT(MCDP_CD) AS "5월예약건수"
    FROM APPOINTMENT
    WHERE APNT_YMD LIKE "2022-05%"
    GROUP BY MCDP_CD
    ) AS T1
ORDER BY T1.5월예약건수, T1.진료과코드;