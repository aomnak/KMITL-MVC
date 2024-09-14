# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from controller.CowController import CowController
from view.WhiteCowView import WhiteCowView
from view.BrownCowView import BrownCowView

class CowCheckApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = CowController()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ระบบตรวจสอบรหัสวัว')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.cow_id_input = QLineEdit(self)
        self.cow_id_input.setPlaceholderText("ป้อนรหัสวัว 8 หลัก")
        layout.addWidget(self.cow_id_input)

        self.submit_btn = QPushButton("ตรวจสอบรหัสวัว", self)
        self.submit_btn.clicked.connect(self.check_cow_id)
        layout.addWidget(self.submit_btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def check_cow_id(self):
        cow_id = self.cow_id_input.text()
        
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id[0] == '0':
            QMessageBox.warning(self, 'ข้อผิดพลาด', 'รหัสไม่ถูกต้อง กรุณาป้อนตัวเลข 8 หลักและไม่ขึ้นต้นด้วย 0')
            return

        cow = self.controller.get_cow_by_id(cow_id)
        if cow is None:
            QMessageBox.warning(self, 'ไม่พบข้อมูล', 'ไม่พบข้อมูลวัวในระบบ')
        else:
            if cow.breed == "white":
                self.view = WhiteCowView(cow, self.controller)
            else:
                self.view = BrownCowView(cow, self.controller)
            self.view.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CowCheckApp()
    window.show()
    sys.exit(app.exec_())
