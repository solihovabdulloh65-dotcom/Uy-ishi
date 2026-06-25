import json
from PyQt5.QtWidgets import *

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = self.load_tasks()

        self.task = QLineEdit()
        self.task.setPlaceholderText("Task nomi")

        self.status = QLineEdit()
        self.status.setPlaceholderText("Done / Pending")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Qidiruv")

        self.btn_add = QPushButton("Qo'shish")
        self.btn_search = QPushButton("Qidirish")
        self.btn_count = QPushButton("Umumiy son")

        self.lbl = QLabel(f"Jami tasklar: {len(self.tasks)}")

        self.btn_add.clicked.connect(self.add_task)
        self.btn_search.clicked.connect(self.search_task)
        self.btn_count.clicked.connect(self.count_task)

        lay = QVBoxLayout()

        for i in [self.task, self.status, self.search,
                  self.btn_add, self.btn_search,
                  self.btn_count, self.lbl]:
            lay.addWidget(i)

        self.setLayout(lay)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        task = self.task.text()
        status = self.status.text()

        if not task or not status:
            QMessageBox.warning(self, "Xato",
                                "Barcha maydonlarni to'ldiring!")
            return

        if status not in ["Done", "Pending"]:
            QMessageBox.warning(self, "Xato",
                                "Status noto'g'ri!")
            return

        self.tasks.append({
            "task": task,
            "status": status
        })

        self.save_tasks()

        self.lbl.setText(
            f"Jami tasklar: {len(self.tasks)}"
        )

        QMessageBox.information(
            self,
            "OK",
            "Task qo'shildi!"
        )

        self.task.clear()
        self.status.clear()

    def search_task(self):
        word = self.search.text()

        if not word:
            QMessageBox.warning(
                self,
                "Habar",
                "Qidiruvga so'z yozing!"
            )
            return

        for i in self.tasks:
            if i["task"].lower() == word.lower():
                QMessageBox.information(
                    self,
                    "Topildi",
                    f"Task: {i['task']}\nStatus: {i['status']}"
                )
                return

        QMessageBox.information(
            self,
            "Natija",
            "Topilmadi!"
        )

    def count_task(self):
        QMessageBox.information(
            self,
            "Umumiy",
            f"Umumiy tasklar soni: {len(self.tasks)}"
        )


app = QApplication([])
win = TaskManager()
win.show()
app.exec_()