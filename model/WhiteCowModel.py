# model/WhiteCowModel.py
from model.CowModel import Cow
import random

class WhiteCow(Cow):
    def __init__(self, cow_id, age_years, age_months):
        super().__init__(cow_id, "white", age_years, age_months)
        self.milk_type = "นมจืด"

    def produce_milk(self, lemon=False): # ตรวจสอบการป้อนมะนาว ถ้าป้อนจะผลิต "นมเปรี้ยว"
        if lemon:
            self.milk_type = "นมเปรี้ยว"
        else:
            if random.random() < 0.005 * self.age_months:
                self.milk_type = "นมถั่วเหลือง"
                self.bsod = True
            else:
                self.milk_type = "นมจืด"
        
        self.milk_bottles += 1
        return self.milk_type
    