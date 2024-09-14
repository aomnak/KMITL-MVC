# view/BrownCowView.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from view.CowReportView import CowReportView

class BrownCowView(QWidget):
    def __init__(self, cow, controller):
        super().__init__()
        self.cow = cow
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel(f"รหัสวัว: {self.cow.cow_id}\nพันธุ์: วัวสีน้ำตาล\nอายุ: {self.cow.age_years} ปี {self.cow.age_months} เดือน")
        layout.addWidget(self.label)

        self.milk_btn = QPushButton('รีดนม')
        self.milk_btn.clicked.connect(self.milk_cow)
        layout.addWidget(self.milk_btn)

        self.setLayout(layout)
        self.setWindowTitle('วัวสีน้ำตาล')

    def milk_cow(self):
        milk_type = self.cow.produce_milk()
        if self.cow.bsod:
            QMessageBox.warning(self, "BSOD", "วัวตัวนี้ผลิตนมไม่ได้แล้ว!")
        else:
            QMessageBox.information(self, "รีดนม", f"วัวผลิต {milk_type}")
        
        # อัปเดตข้อมูลและแสดงรายงานการผลิตนมหลังจากรีดนมเสร็จ
        self.controller.save_cows()
        self.show_report()

    def show_report(self):
        # แสดงรายงานการผลิตนมทันทีหลังจากรีดนมเสร็จ
        self.report_view = CowReportView(self.controller, self)
        self.report_view.show()
