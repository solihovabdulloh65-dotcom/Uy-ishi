import json

from PyQt5.QtWidgets import *



class Malumot(QWidget):
    def __init__(self):
        super().__init__()
    
        self.v_main_lay=QVBoxLayout()

        self.h_lbl_lay=QHBoxLayout()

        self.shahar_tuman_umumiy_lay=QVBoxLayout()

        self.jins_men_women=QHBoxLayout()

        self.shahar_tuman_lay=QHBoxLayout()

        


        self.name=QLineEdit()
        self.name.setPlaceholderText("Name")

        self.second=QLineEdit()
        self.second.setPlaceholderText("Second")

        self.age=QLineEdit()
        self.age.setPlaceholderText("Age")

        self.Jins=QLabel("Jins:")
        self.men=QRadioButton("MAN")
        self.women=QRadioButton("WOMAN")


        self.shahar=QLabel("Shahar")
        self.cmb=QComboBox()
        self.cmb.addItems(["Toshkent","Samarqand","Buxoro","Jizzax","Navoiy","Xorazm","Sirdaryo","Qarshi","Andijon","Qo'qon","Namangan","Surxondaryo"])


        self.cmb.activated[str].connect(self.activated)

        self.cmb2=QComboBox()

        self.btn_submit=QPushButton("submit")
        self.btn_submit.clicked.connect(self.submit)

        self.btn_exit=QPushButton("exit")
        self.btn_exit.clicked.connect(exit)

        self.v_main_lay.addWidget(self.name)
        self.v_main_lay.addWidget(self.second)
        self.v_main_lay.addWidget(self.age)

        self.jins_men_women.addWidget(self.Jins)
        self.jins_men_women.addWidget(self.men)
        self.jins_men_women.addWidget(self.women)

    

        self.shahar_tuman_lay.addWidget(self.shahar)
        self.shahar_tuman_lay.addWidget(self.cmb)
        self.shahar_tuman_lay.addWidget(self.cmb2)



        self.h_lbl_lay.addWidget(self.btn_submit)
        self.h_lbl_lay.addWidget(self.btn_exit)



        self.shahar_tuman_umumiy_lay.addLayout(self.shahar_tuman_lay)

        self.v_main_lay.addLayout(self.jins_men_women)

        self.v_main_lay.addLayout(self.shahar_tuman_umumiy_lay)

        self.v_main_lay.addLayout(self.h_lbl_lay)

        

        self.setLayout(self.v_main_lay)

    def activated(self):
        lst_toshkent=["Yunusobod","Uchtepa","Yashnobod","Shayxontoxur","Olmazor","Chilonzor"]
        lst_andijon=["Asaka","Baliqchi","Bo'z","Buloqboshi","Izboskan","Jalaquduq"]
        lst_Buxoro=["G'ijduvon","Jondor","Kogon","Romitan","Shofirkon","Vobkent"]
        lst_qoqon=["Bag'dod","Furqat","Oltiariq","Rishton","Toshloq","Yozyovon"]
        lst_jizzax=["Arnasoy","Baxmal","G'allaorol","Zafarobod","Zarbdor","Zomin"]
        lst_namangan=["Chortoq","Chust","Norin","Mignbuloq","Uychi","Uchqo'rg'on"]
        lst_navoiy=["Karmana","Konimex","Navbahor","Nurota","Uchquduq","Xatirchi"]
        lst_qarshi=["Chiroqchi","Dehqonobod","g'uzor","Kitob","Muborak","Yakkabog'"]
        lst_samarqand=["Bulung'ur","Ishtixon","Narpay","Nurobod","Qo'shrobod","Urgut"]
        lst_sirdaryo=["Boyovut","Guliston","Oqoltin","Sardoba","Sayxunobod","Xovos"]
        lst_xorazm=["Bog'ot","Gurlan","Xiva","Urganch","Xonqa","Yangibozor"]
        lst_surxondaryo=["Angor","Bandixon","Boysun","Denov","Muzrabot","Sho'rchi"]


        if self.cmb.currentText() == "Toshkent":
            self.cmb2.clear()
            self.cmb2.addItems(lst_toshkent)

        elif self.cmb.currentText() == "Andijon":
            self.cmb2.clear()
            self.cmb2.addItems(lst_andijon)

        elif self.cmb.currentText() == "Buxoro":
            self.cmb2.clear()
            self.cmb2.addItems(lst_Buxoro) 
        
        elif self.cmb.currentText() == "Qo'qon":
            self.cmb2.clear()
            self.cmb2.addItems(lst_qoqon)

        elif self.cmb.currentText() == "Jizzax":
            self.cmb2.clear()
            self.cmb2.addItems(lst_jizzax)

        elif self.cmb.currentText() == "Namangan":
            self.cmb2.clear()
            self.cmb2.addItems(lst_namangan)

        elif self.cmb.currentText() == "Navoiy":
            self.cmb2.clear()
            self.cmb2.addItems(lst_navoiy)
        
        elif self.cmb.currentText() == "Qarshi":
            self.cmb2.clear()
            self.cmb2.addItems(lst_qarshi)
        
        elif self.cmb.currentText() == "Samarqand":
            self.cmb2.clear()
            self.cmb2.addItems(lst_samarqand)

        elif self.cmb.currentText() == "Sirdaryo":
            self.cmb2.clear()
            self.cmb2.addItems(lst_sirdaryo)

        elif self.cmb.currentText() == "Xorazm":
            self.cmb2.clear()
            self.cmb2.addItems(lst_xorazm)

        elif self.cmb.currentText() == "Surxondaryo":
            self.cmb2.clear()
            self.cmb2.addItems(lst_surxondaryo)
            
    def submit(self):
        
        if self.men.isChecked():
            jins="Man"
        else:
            jins="Woman"
        data={
            "name":self.name.text(),
            "second":self.second.text(),
            "age":self.age.text(),
            "jins":jins,
            "shahar":self.cmb.currentText(),
            "tuman":self.cmb2.currentText()
        }

        with open("users.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
        


app=QApplication([])
win=Malumot()
win.show()
app.exec_()