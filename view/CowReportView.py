# view/CowReportView.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class CowReportView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        report = self.controller.generate_report()
        report_text = f"""รายงานการผลิตนม:
        นมจืด: {report['นมจืด']} ขวด
        นมเปรี้ยว: {report['นมเปรี้ยว']} ขวด
        นมช็อกโกแลต: {report['นมช็อกโกแลต']} ขวด
        นมถั่วเหลือง: {report['นมถั่วเหลือง']} ขวด
        นมอัลมอนด์: {report['นมอัลมอนด์']} ขวด"""

        self.label = QLabel(report_text)
        layout.addWidget(self.label)

        # ปุ่มสำหรับรีเซ็ตวัวที่อยู่ในสถานะ BSOD
        self.reset_btn = QPushButton('Reset วัวที่เกิด BSOD')
        self.reset_btn.clicked.connect(self.reset_bsod)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)
        self.setWindowTitle('รายงานการผลิตนม')

    def reset_bsod(self):
        self.controller.reset_bsod()
        QMessageBox.information(self, 'รีเซ็ตสำเร็จ', 'วัวที่เกิด BSOD ถูกรีเซ็ตแล้ว')
