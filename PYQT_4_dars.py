

# 11111111111111111111111111111111111111111111111

# def majority_element(nums:list)->int:
#     if nums == []:
#         return -1
#     else:
#         return max(nums,key=nums.count)


# print(majority_element([3,3,4]))
# print(majority_element([]))


# 222222222222222222222222222222222222

def search_by_genre(cinema:list,genre:str)->list:
    lst=[]
    for i in cinema:
        if i["genre"] in genre:
            lst.append(i)
        
    return lst





cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]



print(search_by_genre(cinema,"Fantastika"))
print("\n")
print(search_by_genre(cinema,"Detektiv"))
print("\n")
print(search_by_genre(cinema,"Komediya"))

# 33333333333333333333333333




#44444444444444444444444444




import json

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout
)


class Movie(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yangi film qo'shish ilovasi")

        self.title = QLineEdit()
        self.director = QLineEdit()
        self.year = QLineEdit()
        self.genre = QLineEdit()

        self.btn = QPushButton("Qo'shish")
        self.btn.clicked.connect(self.add_movie)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Film nomi:"))
        layout.addWidget(self.title)

        layout.addWidget(QLabel("Rejissor:"))
        layout.addWidget(self.director)

        layout.addWidget(QLabel("Yili:"))
        layout.addWidget(self.year)

        layout.addWidget(QLabel("Janr:"))
        layout.addWidget(self.genre)

        layout.addWidget(self.btn)

        self.setLayout(layout)

    def add_movie(self):
        title = self.title.text().strip()
        director = self.director.text().strip()
        year = self.year.text().strip()
        genre = self.genre.text().strip()

        if not title or not director or not year or not genre:
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos, barcha ma'lumotlarni to'ldiring!"
            )
            return

        if not year.isdigit():
            QMessageBox.warning(
                self,
                "Xatolik",
                "Yil raqam bo'lishi kerak!"
            )
            return

        movie = {
            "title": title,
            "director": director,
            "year": int(year),
            "genre": genre
        }

        try:
            with open("movies.json", "r") as file:
                movies = json.load(file)
        except:
            movies = []

        movies.append(movie)

        with open("movies.json", "w") as file:
            json.dump(movies, file, indent=4)

        QMessageBox.information(
            self,
            "Muvaffaqiyatli",
            "Film muvaffaqiyatli qo'shildi!"
        )

        self.title.clear()
        self.director.clear()
        self.year.clear()
        self.genre.clear()


app = QApplication([])

win = Movie()
win.show()

app.exec_()


