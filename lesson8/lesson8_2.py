import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        names_str = file.read()
    names:list[str] = names_str.split(sep='\n')
    names = random.choices(names,k=nums)
    return names

def generate_students(names:list[str]) -> list[dict]:
    students:list[dict] = []
    for name in names:
        chinese = random.randint(50, 100)
        english = random.randint(50, 100)
        math = random.randint(50, 100)
        student = {'name':name,'chinese':chinese,'english':english,'math':math}
        students.append(student)
    return students  
    


nums = int(input('請輸入學生數量(最多10位):'))
student_names:list[str] = get_names(nums=nums)
students:list[dict] = generate_students(names=student_names)
print(students)
