# model/BrownCowModel.py
from model.CowModel import Cow
import random

class BrownCow(Cow):
    def __init__(self, cow_id, age_years, age_months): # กำหนดค่าวัวพันธุ์สีน้ำตาล โดยเริ่มต้นที่ผลิต "นมช็อกโกแลต"
        super().__init__(cow_id, "brown", age_years, age_months)
        self.milk_type = "นมช็อกโกแลต"

    def produce_milk(self): # สุ่มตรวจสอบการผลิต "นมอัลมอนด์" ตามอายุวัว
        if random.random() < 0.01 * self.age_years:
            self.milk_type = "นมอัลมอนด์"
            self.bsod = True # ถ้าผลิตนมอัลมอนด์ จะเข้าสถานะ BSOD
        else:
            self.milk_type = "นมช็อกโกแลต"
        
        self.milk_bottles += 1
        return self.milk_type