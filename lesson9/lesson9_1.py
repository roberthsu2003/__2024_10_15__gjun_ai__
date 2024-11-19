from gear.widget import get_name,generate_bmi

if __name__ == '__main__':
    nums = int(input('請輸入人數:'))
    names:list[str] = get_name(nums=nums)
    students:list[dict] = generate_bmi(names=names)
    for student in students:
        for key,value in student.items():
            print(f'{key}:{value}')
        print("==================")


