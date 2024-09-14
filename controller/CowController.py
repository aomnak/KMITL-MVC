# controller/CowController.py
from model.WhiteCowModel import WhiteCow
from model.BrownCowModel import BrownCow
from model.CowModel import load_cows_data, save_cows_data, generate_report

class CowController:
    def __init__(self, cow_data_file="cows_data.json"):
        self.cows = self.load_cow_data(cow_data_file)
        self.data_file = cow_data_file

    def load_cow_data(self, filename): #โหลดข้อมูลวัวจากไฟล์ JSON และสร้างออบเจ็กต์ WhiteCow หรือ BrownCow ตามข้อมูล
        cows_data = load_cows_data(filename)
        cows = []
        for cow in cows_data:
            if cow["breed"] == "white":
                cows.append(WhiteCow(cow["cow_id"], cow["age_years"], cow["age_months"]))
            elif cow["breed"] == "brown":
                cows.append(BrownCow(cow["cow_id"], cow["age_years"], cow["age_months"]))
        return cows

    def save_cows(self): #บันทึกข้อมูลวัวทั้งหมดในระบบลงในไฟล์ JSON
        save_cows_data(self.cows, self.data_file)

    def get_cow_by_id(self, cow_id): #ค้นหาวัวตามรหัสวัว (cow_id) และคืนค่าวัวนั้น ๆ
        for cow in self.cows:
            if cow.cow_id == cow_id:
                return cow
        return None

    def reset_bsod(self): #ฟังก์ชันนี้ทำหน้าที่รีเซ็ตสถานะ BSOD ของวัวทุกตัวในระบบ
        for cow in self.cows:
            if cow.bsod:
                cow.reset_bsod()
        self.save_cows()

    def generate_report(self): #สร้างรายงานเกี่ยวกับจำนวนขวดนมที่ผลิตโดยวัวแต่ละประเภท
        return generate_report(self.cows)
