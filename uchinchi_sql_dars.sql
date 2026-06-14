CREATE TABLE genre(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE author(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    price INT,
    amount INT,
    g_id INT,
    a_id INT,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO genre(name) VALUES("Roman"), ("Fantastika"), ("Dramma"), ("Tragediya");

INSERT INTO author(name) VALUES("Alisher Navoiy"), ("Pushkin"), ("Bobur"), ("Abdulla Qodiriy");

INSERT INTO book
    (name, price, amount, g_id, a_id) 
VALUES
    ("O'tgan kunlar", 35000, 10, 4, 1),
    ("Shaytanant", 15000, 5, 1, 3),
    ("Hamsa", 150000, 1, 2, 1),
    ("Odam bo'lish qiyin", 10000, 20, 2, 2),
    ("Diqqat", 17000, 2, 3, 4),
    ("12 yil qullikda", 10000, 2, 1, 2),
    ("Jinoyat va jazo", 17000, 8, 4, 1),
    ("Oq kechalar", 25000, 2, 3, 3),
    ("Atom Odatlar", 35000, 3, 2, 4),
    ("Yulduzli tunlar", 39000, 1, 1, 1),
    ("Dunyoning ishlari", 31000, 4, 2, 3),
    ("Kichik Shahzoda", 1000, 5, 1, 2),
    ("Kecha va Kunduz", 19000, 10, 4, 4),
    ("Bilmasvoy", 17000, 5, 2, 1);


-- #1111111111111

SELECT a.name,
    GROUP_CONCAT(DISTINCT g.name) AS genres
FROM book b
JOIN author a on b.a_id=a.id
JOIN genre g on b.g_id=g.id
WHERE a.name='Alisher Navoiy'
GROUP BY a.id,a.name;


+----------------+----------------------------+
| name           | genres                     |
+----------------+----------------------------+
| Alisher Navoiy | Fantastika,Roman,Tragediya |
+----------------+----------------------------+


-- 2222222222222222222222222222



SELECT a.name,
    GROUP_CONCAT(DISTINCT g.name) AS genres
FROM book b
JOIN author a on b.a_id=a.id
JOIN genre g on b.g_id=g.id
GROUP BY a.id,a.name;



+-----------------+-----------------------------+
| name            | genres                      |
+-----------------+-----------------------------+
| Alisher Navoiy  | Fantastika,Roman,Tragediya  |
| Pushkin         | Fantastika,Roman            |
| Bobur           | Dramma,Fantastika,Roman     |
| Abdulla Qodiriy | Dramma,Fantastika,Tragediya |
+-----------------+-----------------------------+


-- 33333333333333333333333333333

SELECT a.name AS autor_name,
       g.name AS genre_name,
       COUNT(*) AS books_count
FROM book b
JOIN author a ON b.a_id=a.id
JOIN genre g ON b.g_id=g.id
GROUP BY a.name,g.name;


+-----------------+------------+-------------+
| autor_name      | genre_name | books_count |
+-----------------+------------+-------------+
| Alisher Navoiy  | Tragediya  |           2 |
| Alisher Navoiy  | Fantastika |           2 |
| Alisher Navoiy  | Roman      |           1 |
| Pushkin         | Fantastika |           1 |
| Pushkin         | Roman      |           2 |
| Bobur           | Roman      |           1 |
| Bobur           | Dramma     |           1 |
| Bobur           | Fantastika |           1 |
| Abdulla Qodiriy | Dramma     |           1 |
| Abdulla Qodiriy | Fantastika |           1 |
| Abdulla Qodiriy | Tragediya  |           1 |
+-----------------+------------+-------------+


-- 44444444444444444444444444444444

SELECT g.name ,
       COUNT(*) AS books_count
FROM book b
JOIN genre g ON b.g_id=g.id
GROUP BY g.id,g.name
ORDER BY books_count DESC
LIMIT 1;

+------------+-------------+
| name       | books_count |
+------------+-------------+
| Fantastika |           5 |
+------------+-------------+

-- 5555555555555555555555555555555

SELECT a.name,
    ->        g.name,
    ->        COUNT(*) AS book_count
    -> FROM book b
    -> JOIN author a ON b.a_id = a.id
    -> JOIN genre g ON b.g_id = g.id
    -> GROUP BY a.id, g.id
    -> ORDER BY a.name, book_count DESC;
+-----------------+------------+------------+
| name            | name       | book_count |
+-----------------+------------+------------+
| Abdulla Qodiriy | Dramma     |          1 |
| Abdulla Qodiriy | Fantastika |          1 |
| Abdulla Qodiriy | Tragediya  |          1 |
| Alisher Navoiy  | Tragediya  |          2 |
| Alisher Navoiy  | Fantastika |          2 |
| Alisher Navoiy  | Roman      |          1 |
| Bobur           | Roman      |          1 |
| Bobur           | Dramma     |          1 |
| Bobur           | Fantastika |          1 |
| Pushkin         | Roman      |          2 |
| Pushkin         | Fantastika |          1 |
+-----------------+------------+------------+


-- 6666666666666666666666666666666666666666666

SELECT a.name,b.name,b.amount
FROM book b
JOIN author a on b.a_id=a.id
ORDER BY b.amount DESC
LIMIT 1;

+---------+--------------------+--------+
| name    | name               | amount |
+---------+--------------------+--------+
| Pushkin | Odam bolish qiyin |     20 |
+---------+--------------------+--------+