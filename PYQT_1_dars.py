from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout







class calkulyator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculyator")

        self.v_main_lay=QVBoxLayout()
        self.h_lbl_lay=QHBoxLayout()

        self.son1=QLineEdit()
        self.son2=QLineEdit()

        self.btn_plus=QPushButton("+")
        self.btn_minus=QPushButton("-")
        self.btn_mult=QPushButton("*")
        self.btn_div=QPushButton("/")

        self.lbl_natija=QLabel("Natija")

        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_div.clicked.connect(self.div)

       

        self.v_main_lay.addWidget(self.son1)
        self.v_main_lay.addWidget(self.son2)

        self.h_lbl_lay.addWidget(self.btn_plus)
        self.h_lbl_lay.addWidget(self.btn_minus)
        self.h_lbl_lay.addWidget(self.btn_mult)
        self.h_lbl_lay.addWidget(self.btn_div)

        self.v_main_lay.addWidget(self.lbl_natija)

        self.v_main_lay.addLayout(self.h_lbl_lay)

        self.setLayout(self.v_main_lay)

    def plus(self):
        a=int(self.son1.text())
        b=int(self.son2.text())

        self.lbl_natija.setText(f"Natija:{a+b}")

        self.son1.clear()
        self.son2.clear()
    def minus(self):
        a=int(self.son1.text())
        b=int(self.son2.text())

        self.lbl_natija.setText(f"Natija:{a-b}")
        
        self.son1.clear()
        self.son2.clear()
    def mult(self):
        a=int(self.son1.text())
        b=int(self.son2.text())

        self.lbl_natija.setText(f"Natija:{a*b}")
        
        self.son1.clear()
        self.son2.clear()
    def div(self):
        a=int(self.son1.text())
        b=int(self.son2.text())

        self.lbl_natija.setText(f"Natija:{a//b}")
        
        
        self.son1.clear()
        self.son2.clear()







app=QApplication([])
win=calkulyator()
win.show()
app.exec_()


