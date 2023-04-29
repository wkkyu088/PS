SELECT T2.PRODUCT_CODE, T2.PRICE*SUM(T1.SALES_AMOUNT) AS SALES
FROM OFFLINE_SALE AS T1
JOIN PRODUCT AS T2 ON T1.PRODUCT_ID = T2.PRODUCT_ID
GROUP BY T2.PRODUCT_CODE
ORDER BY SALES DESC, T2.PRODUCT_CODE