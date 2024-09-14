# model/CowModel.py
import json

class Cow:
    def __init__(self, cow_id, breed, age_years, age_months): # กำหนดคุณสมบัติพื้นฐานของวัว
        self.cow_id = cow_id
        self.breed = breed
        self.age_years = age_years
        self.age_months = age_months
        self.milk_bottles = 0
        self.bsod = False  # สถานะ BSOD

    def get_age(self):
        return self.age_years + (self.age_months / 12)

    def reset_bsod(self):
        self.bsod = False

def load_cows_data(filename="cows_data.json"):
    with open(filename, 'r') as file:
        cows_data = json.load(file)
    return cows_data

def save_cows_data(cows, filename="cows_data.json"):
    cows_data = []
    for cow in cows:
        cow_data = {
            "cow_id": cow.cow_id,
            "breed": cow.breed,
            "age_years": cow.age_years,
            "age_months": cow.age_months,
            "milk_bottles": cow.milk_bottles,
            "bsod": cow.bsod,
            "milk_type": cow.milk_type
        }
        cows_data.append(cow_data)
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(cows_data, file, indent=4, ensure_ascii=False)


def generate_report(cows):
    total_milk_bottles = {"นมจืด": 0, "นมเปรี้ยว": 0, "นมช็อกโกแลต": 0, "นมถั่วเหลือง": 0, "นมอัลมอนด์": 0}
    for cow in cows:
        if cow.breed == "white":
            if cow.bsod:
                total_milk_bottles["นมถั่วเหลือง"] += cow.milk_bottles
            else:
                total_milk_bottles["นมจืด"] += cow.milk_bottles
        elif cow.breed == "brown":
            if cow.bsod:
                total_milk_bottles["นมอัลมอนด์"] += cow.milk_bottles
            else:
                total_milk_bottles["นมช็อกโกแลต"] += cow.milk_bottles
    return total_milk_bottles
