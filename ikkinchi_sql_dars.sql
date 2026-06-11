CREATE DATABASE dokon;


CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    sale_date DATE
);


--------------------------------------------------
INSERT INTO sales VALUES (1, 'Laptop', 'Electronics', 800, 2, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 'Electronics', 600, 3, '2025-01-01');
INSERT INTO sales VALUES (3, 'TV', 'Electronics', 900, 1, '2025-01-02');
INSERT INTO sales VALUES (4, 'Headphones', 'Electronics', 150, 5, '2025-01-03');
INSERT INTO sales VALUES (5, 'Table', 'Furniture', 300, 1, '2025-01-01');
INSERT INTO sales VALUES (6, 'Chair', 'Furniture', 100, 4, '2025-01-02');
INSERT INTO sales VALUES (7, 'Sofa', 'Furniture', 1200, 1, '2025-01-03');
INSERT INTO sales VALUES (8, 'Bed', 'Furniture', 900, 1, '2025-01-04');
INSERT INTO sales VALUES (9, 'T-shirt', 'Clothing', 40, 6, '2025-01-01');
INSERT INTO sales VALUES (10, 'Jeans', 'Clothing', 70, 3, '2025-01-02');
INSERT INTO sales VALUES (11, 'Jacket', 'Clothing', 120, 2, '2025-01-03');
INSERT INTO sales VALUES (12, 'Shoes', 'Clothing', 90, 4, '2025-01-04');
INSERT INTO sales VALUES (13, 'Apple', 'Food', 2, 20, '2025-01-01');
INSERT INTO sales VALUES (14, 'Bread', 'Food', 3, 15, '2025-01-02');
INSERT INTO sales VALUES (15, 'Milk', 'Food', 4, 10, '2025-01-03');
INSERT INTO sales VALUES (16, 'Cheese', 'Food', 8, 5, '2025-01-04');
INSERT INTO sales VALUES (17, 'Notebook', 'Stationery', 5, 10, '2025-01-01');
INSERT INTO sales VALUES (18, 'Pen', 'Stationery', 2, 25, '2025-01-02');
INSERT INTO sales VALUES (19, 'Marker', 'Stationery', 4, 12, '2025-01-03');
INSERT INTO sales VALUES (20, 'Folder', 'Stationery', 6, 8, '2025-01-04');




-- 111111111. Har bir kategoriya bo'yicha nechta mahsulot sotilganini toping.

SELECT category,COUNT(*) as miqdor,SUM(quantity) as sotilgan_maxsulot FROM sales GROUP BY category;

+-------------+--------+-------------------+
| category    | miqdor | sotilgan_maxsulot |
+-------------+--------+-------------------+
| Electronics |      4 |                11 |
| Furniture   |      4 |                 7 |
| Clothing    |      4 |                15 |
| Food        |      4 |                50 |
| Stationery  |      4 |                55 |
+-------------+--------+-------------------+



--22222222222. Har bir kategoriya boâ€˜yicha jami sotuv summasini chiqaring.

SELECT category,COUNT(*) as miqdor,sum(price*quantity) as jami_sotuv_summasi from sales GROUP BY category;

+-------------+--------+--------------------+
| category    | miqdor | jami_sotuv_summasi |
+-------------+--------+--------------------+
| Electronics |      4 |               5050 |
| Furniture   |      4 |               2800 |
| Clothing    |      4 |               1050 |
| Food        |      4 |                165 |
| Stationery  |      4 |                196 |
+-------------+--------+--------------------+



--333333333333333333333. Har bir kategoriya boâ€˜yicha o'rtacha narxni hisoblang.

SELECT category, AVG(price*quantity) as ortacha_narx,SUM(price*quantity) as jami_narx from sales GROUP BY category;

+-------------+--------------+-----------+
| category    | ortacha_narx | jami_narx |
+-------------+--------------+-----------+
| Electronics |    1262.5000 |      5050 |
| Furniture   |     700.0000 |      2800 |
| Clothing    |     262.5000 |      1050 |
| Food        |      41.2500 |       165 |
| Stationery  |      49.0000 |       196 |
+-------------+--------------+-----------+




--444444444. Har bir kun bo'yicha jami tushumni toping.


SELECT sale_date,SUM(price*quantity) as jami_tushum from sales GROUP BY sale_date;

+------------+-------------+
| sale_date  | jami_tushum |
+------------+-------------+
| 2025-01-01 |        4030 |
| 2025-01-02 |        1605 |
| 2025-01-03 |        2278 |
| 2025-01-04 |        1348 |
+------------+-------------+




--55555555555. Faqat Electronics kategoriyasidagi mahsulotlar bo'yicha umumiy tushumni hisoblang.

SELECT category,SUM(price*quantity) as jami_tushum from sales GROUP BY category having category = "electronics";

+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |        5050 |
+-------------+-------------+



--6666666666666. Jami sotuv summasi 2000 dan katta bo'lgan kategoriyalarni chiqaring.


SELECT category,SUM(price*quantity) as jami_sotuv_summasi from sales GROUP BY category having sum(price)>2000;

+-------------+--------------------+
| category    | jami_sotuv_summasi |
+-------------+--------------------+
| Electronics |               5050 |
| Furniture   |               2800 |
+-------------+--------------------+



--777777777777. O'rtacha narxi 100 dan yuqori bo'lgan kategoriyalarni toping.

select category,AVG(price*quantity) as ortacha_narx from sales GROUP BY category HAVING avg(price)>100; 

+-------------+--------------+
| category    | ortacha_narx |
+-------------+--------------+
| Electronics |    1262.5000 |
| Furniture   |     700.0000 |
+-------------+--------------+




--8888888888. 2025-01-01 sanasida nechta mahsulot sotilganini aniqlang.

SELECT sale_date,sum(quantity) as jami_sotilgan_maxsulot from sales GROUP BY sale_date HAVING sale_date="2025-01-01";

+------------+------------------------+
| sale_date  | jami_sotilgan_maxsulot |
+------------+------------------------+
| 2025-01-01 |                     42 |
+------------+------------------------+





--9999999999999. Eng ko'p miqdorda (quantity) sotilgan kategoriyani toping.

SELECT category,sum(quantity) as eng_kop_sotilgan from sales GROUP BY category order by sum(quantity)  desc limit 1;

+------------+------------------+
| category   | eng_kop_sotilgan |
+------------+------------------+
| Stationery |               55 |
+------------+------------------+



--10 10 10 10 10. 3 martadan ko'p sotilgan (quantity > 3) mahsulotlar bo'yicha kategoriyalar kesimida jami tushumni chiqaring.

select  category,SUM(price*quantity) as jami_tushum from sales WHERE quantity > 3 GROUP BY category;

+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |         750 |
| Furniture   |         400 |
| Clothing    |         600 |
| Food        |         165 |
| Stationery  |         196 |
+-------------+-------------+