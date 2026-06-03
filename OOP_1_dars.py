#111111111111111111111111111111111111111111111111

# class Kitob:
#     def __init__(self,nomi,muallifi,narxi,nashriyot):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.narxi=narxi
#         self.nashriyot=nashriyot
#     def chiq(self):
#         print(
#             self.nomi,
#             self.muallifi,
#             self.narxi,
#             self.nashriyot
#         )




# k1=Kitob("Adabiyot","Ahmad",40000,"Anor")
# k2=Kitob("Kimyo","Davron",50000,"Uzum")
# k3=Kitob("Ona tili","Madina",80000,"Hurmo")
# k4=Kitob("Zoologiya","Azamat",40000,"Nur")
# k5=Kitob("Botanika","Bobur",40000,"Ziyo")


# lst=[k1,k2,k3,k4,k5]

# for i in lst:
#     if "A" <=i.nashriyot[0].upper() <="H":
#         i.chiq()
    
    

#22222222222222222222222222222222222222222

# class Kompyuter:
#     def __init__(self,nomi,ram,narxi,protsessori):
#         self.nomi=nomi
#         self.ram=ram
#         self.narxi=narxi
#         self.protsessori=protsessori
#     def raqam(self):
#         print(
#             self.nomi,
#             self.ram,
#             self.narxi,
#             self.protsessori
#         )

# k1=Kompyuter("Dell",12,350,"i3")
# k2=Kompyuter("HP",4,300,"i3")
# k3=Kompyuter("Asus",16,550,"i9")
# k4=Kompyuter("Apple",8,700,"i7")
# k5=Kompyuter("Lenova",4,250,"i5")

# lst=[k1,k2,k3,k4,k5]

# for i in lst:
#     if 4 < i.ram <16:
#         i.raqam()



#33333333333333333333333333333333333333333

class User:
    def __init__(self,ism,login,email):
        self.ism=ism
        self.login=login
        self.email=email
    def get_info(self):
        print(f"""
Foydalanuvchi:{self.login}
Ismi:{self.ism}
email:{self.email}   
        """)
    

u1=User("Ali Valiyev","alijon123","ali@gmail.com")
u2=User("Odil ahmedov","odiljon987","odil765@gmail.com")
u3=User("Husan hasanov","husun012","husun123@gmail.com")

u1.get_info()
u2.get_info()
u3.get_info()