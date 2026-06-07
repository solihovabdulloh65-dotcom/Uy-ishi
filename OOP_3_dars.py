class MyDate:
    Oylar=["Yanvar","Fevral","Mart","Aprel",
    "May","Iyun","Iyul","Avgust",
    "Sentabr","Oktabr","Noyabr","Dekabr"]
    def __init__(self,day,month,year):
        if not self.isValidDate(day,month,year):
            raise ValueError("Notog'ri sana kiritildi!")
        self.__day=day
        self.__month=month
        self.__year=year
    @staticmethod

    def isLeapyear(year):
        return (
            year % 400==0 or
            (year % 4==0 and year % 100 !=0)
        )
    @classmethod

    def isValidDate(cls,day,month,year):
        if not (1<=year<=9999):
            return False
        if not (1<=month<=12):
            return False
        days=[31,28,31,30,31,30,
              31,31,30,31,30,31]
        if cls.isLeapyear(year):
            days[1]=29
        return 1<=day <=days[month-1]

    def setDate(self,day,month,year):
        if not self.isValidDate(day,month,year):
            raise ValueError ("Noto'g'ri sana kiritldi!")
        self.__day=day
        self.__month=month
        self.__year=year

    def nextDay(self):
        days=[31,28,31,30,31,30,
              31,31,30,31,30,31]
        if self.isLeapyear(self.__year):
            days[1]=29
        self.__day+=1

        if self.__day>days[self.__month-1]:
            self.__day=1
            self.__month+=1
            if self.__month>12:
                self.__month=1
                self.__year+=1
        return self

    def previousDay(self):
        days=[31,28,31,30,31,30,
              31,31,30,31,30,31]
        if self.isLeapyear(self.__year):
            days[1]=29
        self.__day-=1
        if self.__day<1:
            self.__month-=1
            if self.__month<1:
                self.__month=12
                self.__year-=1
            days=[31,28,31,30,31,30,
                  31,31,30,31,30,31]
            if self.isLeapyear(self.__year):
                days[1]=29
            self.__day=days[self.__month-1]
        return self

    def nextMonth(self):
        month=self.__month+1
        year=self.__year
        if month > 12:
            month=1
            year+=1
        days=[31,28,31,30,31,30,
              31,31,30,31,30,31]
        if self.isLeapyear(year):
            days[1]=29
        day=min(self.__day,days[month-1])
        self.__day=day
        self.__month=month
        self.__year=year
        return self

    def previousMonth(self):
        month=self.__month-1
        year=self.__year
        if month<1:
            month=12
            year-=1
        days=[31,28,31,30,31,30,
              31,31,30,31,30,31]
        if self.isLeapyear(year):
            days[1]=29
        day=min(self.__day,days[month-1])
        self.__day=day
        self.__month=month
        self.__year=year
        return self

    def nextYear(self):
        year=self.__year+1
        day=self.__day
        month=self.__month
        if month ==2 and day==29 and not self.isLeapyear(year):
            day=28
        self.__day=day
        self.__year=year
        return self
    def previousYear(self):
        year=self.__year-1
        if year < 1:
            raise ValueError("Yil 1 dan kichik bo'lishi mumkin emas")
        day=self.__day
        month=self.__month
        if month==2 and day==29 and not self.isLeapyear(year):
            day=28
        self.__day=day
        self.__year=year
        return self
    def __str__(self):
        return(
            f"{self.__day:02d}-"
            f"{self.Oylar[self.__month-1]} "
            f"{self.__year} yil"
        )



print("Ertangi kunga o'zgardi")
sana=MyDate(15, 6, 2023)
print(sana)
sana.nextDay()
print(sana)

print("\n")

print("Ertangi kunga o'zgardi oyning oxiri bo'lgani uchun keyingi oyga o'tdi")
sana=MyDate(30,4,2023)
print(sana)
sana.nextDay()
print(sana)

print("\n")

print("Ertangi kunga o'zgardi oyning oxiri va yilning oxiri bo'lgani uchun keyingi oyga va yilga o'tdi")
sana=MyDate(31,12,2023)
print(sana)
sana.nextDay()
print(sana)

print("\n")

print("Bir kun ortga o'zgardi")
sana=MyDate(1,5,2023)
print(sana)
sana.previousDay()
print(sana)

print("\n")

print("Kabisa yili bo'lgani uchun 29 ga o'zgardi")
sana=MyDate(28,2,2024)
print(sana)
sana.nextDay()
print(sana)

print("\n")

print("Kabisa yili va oy o'zgardi")
sana=MyDate(29,2,2024)
print(sana)
sana.nextDay()
print(sana)

print("\n")


print("Kabisa yili bo'lmagani uchun oy o'zgardi")
sana=MyDate(28,2,2023)
print(sana)
sana.nextDay()
print(sana)

print("\n")

print("Oy boshi bo'lgani uchun oldingi yil oxiriga o'zgardi")
sana=MyDate(1,1,2023)
print(sana)
sana.previousDay()
print(sana)

print("\n")

print("Faqat oyga 1 qo'shildi")
sana=MyDate(15,6,2024)
print(sana)
sana.nextMonth()
print(sana)

print("\n")

print("Faqat oydan 1 ayrildi")
sana=MyDate(15,6,2024)
print(sana)
sana.previousMonth()
print(sana)

print("\n")

print("Faqat yilga 1 qo;shildi")
sana=MyDate(15,6,2024)
print(sana)
sana.nextYear()
print(sana)

print("\n")

print("Faqat yildan 1 ayrildi")
sana=MyDate(15,6,2024)
print(sana)
sana.previousYear()
print(sana)