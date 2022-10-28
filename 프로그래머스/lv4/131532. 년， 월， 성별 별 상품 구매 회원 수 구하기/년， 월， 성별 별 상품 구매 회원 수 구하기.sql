SELECT EXTRACT(YEAR FROM B.SALES_DATE) AS YEAR,
    EXTRACT(MONTH FROM B.SALES_DATE) AS MONTH,
    A.GENDER,
    COUNT(DISTINCT A.USER_ID) AS USERS
FROM USER_INFO A
INNER JOIN ONLINE_SALE B
ON A.USER_ID = B.USER_ID
WHERE A.GENDER IS NOT NULL
GROUP BY EXTRACT(YEAR FROM B.SALES_DATE), EXTRACT(MONTH FROM B.SALES_DATE), A.GENDER
ORDER BY YEAR, MONTH, GENDER