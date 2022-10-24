import User_interfase as ui
def see_data():
    with open("InfoStudent.csv", 'r') as f:
        for line in f:
            print(line)

def search_students():
    
    fopen = open('InfoStudent.csv',mode='r+')

    fread = fopen.readlines()

    x = input("Введите ключевую информацию о студенте:  ").lower()

    for line in fread:
        if x in line:
            print(line)
def again():
    print("Вернуться в предыдущее меню? 'Y' - Yes, 'N' - No")

    res = input()
    if res.upper() == 'Y':
        return ui.result_opt()
    elif res.upper() == 'N':
        print("До встречи!")
    else:
        if res.upper() != 'Y' or res.upper() != 'N':
            print("Ошибка ввода") 
            return again()

