SELECT month(start_date) AS MONTH, car_id AS CAR_ID, count(history_id) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id IN (
    SELECT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE date(start_date) >= '2022-08-01' AND date(start_date) < '2022-11-01'
    GROUP BY car_id
    HAVING count(history_id) >= 5
) AND date(start_date) >= '2022-08-01' AND date(start_date) < '2022-11-01'
GROUP BY car_id, month(start_date)
ORDER BY month(start_date), car_id DESC;