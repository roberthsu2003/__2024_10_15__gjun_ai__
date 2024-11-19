from gear import widget
if __name__ == '__main__':
    nums = int(input('請輸入人數:'))
    names:list[str] = widget.get_name(nums=nums)
    students:list[dict] = widget.generate_bmi(names=names)
    for student in students:
        for key,value in student.items():
            print(f'{key}:{value}')
        print("==================")


