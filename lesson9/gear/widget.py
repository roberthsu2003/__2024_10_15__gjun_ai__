import random

def get_name(nums:int=2)->list[str]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names_str = file.read()
    names = names_str.split()
    names = random.choices(names,k=nums)
    return  names

def generate_bmi(names:list[str])->list[dict]:
    students:list[dict] = []
    for name in names:
        height = random.randint(140,190)
        weight = random.randint(50,110)
        BMI = weight / ((height/100)**2)
        if BMI >= 35:
            status = "重度肥胖"
        elif BMI >= 30:
            status = "中度肥胖"
        elif BMI >= 27:
            status = "輕度肥胖"
        elif BMI >= 24:
            status = "過重"
        elif BMI >= 18.5:
            status = "正常範圍"
        else:
            status = "體重過輕"
        student = {
            '姓名':name,
            '身高':height,
            '體重':weight,
            'BMI':round(BMI,2),
            '狀態':status
        }
        students.append(student)
    return students
