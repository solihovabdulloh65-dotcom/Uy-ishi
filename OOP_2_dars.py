
1111111111111111111111111111

class playlist:
    def __init__(self,owner):
        self.owner=owner
        self.track=[]
    def add_track(self,title,artist):
        self.track.append((title,artist))
    def remove_last(self):
        if self.track:
            return self.track.pop()
    def total_track(self):
        return len(self.track)
    def unique_track(self):
        natija=[]
        for i in self.track:
            if i not in natija:
                natija.append(i)
        return natija
    def search_by_title(self,title):
        natija=[]
        for x, i in self.track:
            if x==title:
                natija.append((x,i))
        return natija
    def filter_by_artist(self,artist):
        natija=[]
        for x,i in self.track:
            if i == artist:
                natija.append((x,i))
        return natija

p1=playlist("Muhammad")
print(p1.total_track())

p1.add_track("Yomg'irlar","Shahzoda")
p1.add_track("Gulim","Yulduz usmonova")
p1.add_track("Yomg'irlar","Shahzoda")
p1.add_track("Xayr endi","Lola")
p1.add_track("Kel","Ulug'bek rahmatullayev")

print(p1.total_track())
print(p1.unique_track())
print(p1.remove_last())
print(p1.total_track())
print(p1.search_by_title("Yomg'irlar"))
print(p1.filter_by_artist("Yulduz usmonova"))




#22222222222222222222222222222222222222222


# class Employee:
#     def __init__(self,name:str,employee_id:str,hourly_rate:float=15.0):
#         self.name=name
#         self.employee_id=employee_id
#         self.working_hours=[]
#         self.hourly_rate=hourly_rate
    
  
#     def log_hours(self,hour:int):
#         if 0<=hour<=24:
#             self.working_hours.append(hour)
#             return True
#         else:
#             return False
    
#     def total_hours(self):
#         return sum(self.working_hours)

#     def calculate_salary(self):
#         natija=sum(self.working_hours)*self.hourly_rate
#         return natija
        
#     def reset_hours(self):
#         self.working_hours=[]








# e1=Employee("Javlon","E101",hourly_rate=20.0)

# print(e1.log_hours(8))
# print(e1.log_hours(9))
# print(e1.log_hours(10))
# print(e1.log_hours(25))


# print(e1.total_hours())
# print(e1.calculate_salary())

# e1.reset_hours()
# print(e1.total_hours())
# print(e1.calculate_salary())





#333333333333333333333333333333333333333333333333

# class Student:
#     def __init__(self,name:str,student_id:str):
#         self.name=name
#         self.student_id=student_id
#         self.grades_list=[]
#     def add_grade(self,grade):
#         if 0<=grade<=100:
#             self.grades_list.append(grade)
#         else:
#             print("Xato baho")
#     def calculate_avarge(self):
#         if not self.grades_list:
#             return 0
#         return sum(self.grades_list)/len(self.grades_list)
        
#     def get_status(self):
#         natija=self.calculate_avarge()
#         if 90<=natija:
#             return "A'lo"
#         elif 80<=natija:
#             return "Yaxshi"
#         elif 70<=natija:
#             return "Qoniqarli"
#         elif natija<70:
#             return "Qoniqarsiz"
#     def info(self):
#         print(f"""Ism:{self.name}
# ID:{self.student_id}""")



# s1=Student("Nodira","S123")
# s1.info()

# s1.add_grade(85)
# s1.add_grade(90)

# print(s1.calculate_avarge())
# print(s1.get_status())

# s1.add_grade(150)

# print("\nYangi student\n")

# s2=Student("Bobur","s124")
# s2.info()

# s2.add_grade(90)
# s2.add_grade(92)

# print(s2.calculate_avarge())
# print(s2.get_status())


# print("\nYangi student\n")

# s3=Student("Vali","s125")
# s3.info()

# s3.add_grade(60)
# s3.add_grade(70)

# print(s3.calculate_avarge())
# print(s3.get_status())
