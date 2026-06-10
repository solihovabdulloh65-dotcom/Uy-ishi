CREATE DATABASE IF NOT EXISTS NOUTBOOK;


CREATE TABLE laptops(
    id int  primary key auto_increment,
    brand VARCHAR(50),
    model VARCHAR(50),
    cpu VARCHAR(50),
    frequency DECIMAL(2,1),
    ram int,
    os VARCHAR(50),
    price DECIMAL(10,2) 
);


                          



INSERT INTO laptops(brand,model,cpu,frequency,ram,os,price)VALUES
                          ("Dell","incpiron 15","intel core i5-1235u",4.4,8,"windows 11",650),
                          ("Dell","vostro 3520","intel core i3-1235u",4.4,16,"windows 11",780),
                          ("HP","pavilion 15","intel core i7-1255u",4.7,16,"windows 10",900),
                          ("HP","250 g9","intel core i5-1235u",4.8,8,"windows 11",700),
                          ("lenova","idea pad3","amp ryzan 5",4.0,8,"windows 11",620),
                          ("lenova","sincbook 15","amd ryzan 3",4.0,4,"windows 11",750),
                          ("apple","macbook air m2","apple m2",3.5,8,"macos",1100),
                          ("apple","macbook pro 14","apple m2 pro",3.7,8,"macos",1900),
                          ("asus","vivo book 15","intel core i5-1235u",4.4,16,"windows 11",670),
                          ("asus","zenbook 14","intel core i7-1235u",4.7,16,"windows 11",1050);


#11111111111111111111111111111111111111111111

select *from laptops order by price desc LIMIT 1; 

+----+-------+----------------+--------------+-----------+------+-------+---------+
| id | brand | model          | cpu          | frequency | ram  | os    | price   |
+----+-------+----------------+--------------+-----------+------+-------+---------+
|  8 | apple | macbook pro 14 | apple m2 pro |       3.7 |    8 | macos | 1900.00 |
+----+-------+----------------+--------------+-----------+------+-------+---------+




#22222222222222222222222222222222222222222222

select *from laptops order by price LIMIT 1;

+----+--------+-----------+-------------+-----------+------+------------+--------+
| id | brand  | model     | cpu         | frequency | ram  | os         | price  |
+----+--------+-----------+-------------+-----------+------+------------+--------+
|  5 | lenova | idea pad3 | amp ryzan 5 |       4.0 |    8 | windows 11 | 620.00 |
+----+--------+-----------+-------------+-----------+------+------------+--------+



#333333333333333333333333333333333333333333333333

select frequency from laptops  where price>=400 and price <=1000 AND cpu LIKE "%intel%";


+----+-------+--------------+---------------------+-----------+------+------------+--------+
| id | brand | model        | cpu                 | frequency | ram  | os         | price  |
+----+-------+--------------+---------------------+-----------+------+------------+--------+
|  1 | Dell  | incpiron 15  | intel core i5-1235u |       4.4 |    8 | windows 11 | 650.00 |
|  2 | Dell  | vostro 3520  | intel core i3-1235u |       4.4 |   16 | windows 11 | 780.00 |
|  3 | HP    | pavilion 15  | intel core i7-1255u |       4.7 |   16 | windows 10 | 900.00 |
|  4 | HP    | 250 g9       | intel core i5-1235u |       4.8 |    8 | windows 11 | 700.00 |
|  9 | asus  | vivo book 15 | intel core i5-1235u |       4.4 |   16 | windows 11 | 670.00 |
+----+-------+--------------+---------------------+-----------+------+------------+--------+


faqat frequency

+-----------+
| frequency |
+-----------+
|       4.4 |
|       4.4 |
|       4.7 |
|       4.8 |
|       4.4 |
+-----------+


#444444444444444444444444444444444444444444444444444444
select * from laptops where brand = "apple";

+----+-------+----------------+--------------+-----------+------+-------+---------+
| id | brand | model          | cpu          | frequency | ram  | os    | price   |
+----+-------+----------------+--------------+-----------+------+-------+---------+
|  7 | apple | macbook air m2 | apple m2     |       3.5 |    8 | macos | 1100.00 |
|  8 | apple | macbook pro 14 | apple m2 pro |       3.7 |    8 | macos | 1900.00 |
+----+-------+----------------+--------------+-----------+------+-------+---------+



#555555555555555555555555555555555555555555555555555555

select * from laptops where os LIKE "windows%" and ram=16 and brand='asus' order by price;

+----+-------+--------------+---------------------+-----------+------+------------+---------+
| id | brand | model        | cpu                 | frequency | ram  | os         | price   |
+----+-------+--------------+---------------------+-----------+------+------------+---------+
|  9 | asus  | vivo book 15 | intel core i5-1235u |       4.4 |   16 | windows 11 |  670.00 |
| 10 | asus  | zenbook 14   | intel core i7-1235u |       4.7 |   16 | windows 11 | 1050.00 |
+----+-------+--------------+---------------------+-----------+------+------------+---------+