import pymysql

class MYSQL1:
    def __init__(self):
        self.connectDB()
        self.CreateDB()
        self.CreateTB()
    def connectDB(self):
        self.db=pymysql.connect(
            host='localhost',
            user='root',
            password="1234"
        )
        self.c=self.db.cursor()
    def CreateDB(self):
        self.c.execute('''CREATE DATABASE IF NOT EXISTS vazifa''')
        self.c.execute('''USE vazifa''')
    def CreateTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS restoranlar(
        id int auto_increment primary key,
        name VARCHAR(50) not null,
        adress VARCHAR(50) not null,
        maxFoodPrice DECIMAL(10,2) not null,
        minFoodPrice DECIMAL(10,2) not null,
        employeesCount int DEFAULT 1,
        experience int not null
        )''')
    def InsertTB(self):
        self.c.execute(f'''INSERT INTO restoranlar(
        name,adress,maxFoodPrice,minFoodPrice,employeesCount,experience)
        VALUES
        ("Majbur","Toshkent",120000,25000,25,10),
        ("Mirador","Samarqand",150000,30000,30,15),
        ("Marmar","Buxoro",100000,20000,18,8),
        ("Mister","Andijon",180000,40000,35,20),
        ("Saxovat","Namangan",90000,15000,12,5),
        ("Rayhon","Farg'ona",110000,22000,20,7),
        ("Mashhur","Navoiy",140000,28000,28,12),
        ("Mehr","Qarshi",130000,26000,22,9),
        ("Osh Markazi","Jizzax",80000,12000,15,4),
        ("Motor","Urganch",160000,35000,32,18)''')
        self.db.commit()
    def nomi(self):
        self.c.execute(f'''SELECT *FROM restoranlar 
        where LOWER(name) like "m%r" order by maxFoodPrice''')
        return self.c.fetchall()
    def eng_kam_pul(self):
        self.c.execute(f'''SELECT name,minFoodPrice 
        from restoranlar order by minFoodPrice limit 3''')
        return self.c.fetchall()
    def tajriba(self):
        self.c.execute(f'''SELECT name,maxFoodPrice,experience from restoranlar
        order by experience desc limit 4''')
        return self.c.fetchall()
    
mysql=MYSQL1()
# mysql.InsertTB()

#11111111111111111111111111111111111111111111111
print("1-masala")
for i in mysql.nomi():
    print(i)


# (3, 'Marmar', 'Buxoro', Decimal('100000.00'), Decimal('20000.00'), 18, 8)
# (1, 'Majbur', 'Toshkent', Decimal('120000.00'), Decimal('25000.00'), 25, 10)
# (8, 'Mehr', 'Qarshi', Decimal('130000.00'), Decimal('26000.00'), 22, 9)
# (7, 'Mashhur', 'Navoiy', Decimal('140000.00'), Decimal('28000.00'), 28, 12)
# (2, 'Mirador', 'Samarqand', Decimal('150000.00'), Decimal('30000.00'), 30, 15)
# (10, 'Motor', 'Urganch', Decimal('160000.00'), Decimal('35000.00'), 32, 18)
# (4, 'Mister', 'Andijon', Decimal('180000.00'), Decimal('40000.00'), 35, 20)


#222222222222222222222222222222222222222222222222222222
print("2-masala")
for i in mysql.eng_kam_pul():
    print(i)

# ('Osh Markazi', Decimal('12000.00'))
# ('Saxovat', Decimal('15000.00'))
# ('Marmar', Decimal('20000.00'))

#3333333333333333333333333333333333333333333333333333333333
print("3-masala")
for i in mysql.tajriba():
    print(i)

# ('Mister', Decimal('180000.00'), 20)
# ('Motor', Decimal('160000.00'), 18)
# ('Mirador', Decimal('150000.00'), 15)
# ('Mashhur', Decimal('140000.00'), 12)