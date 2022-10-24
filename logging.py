from datetime import datetime as dt
import User_interfase as ui


def loger_stud(data1,data2,data3,data4):
    time = dt.now().strftime('%D;%H:%M')
    with open('InfoStudent.csv', 'a') as file:
        file.write('{};Name:{};Sername:{};DataOfbirth:{};Group{}\n'
                    .format(time,data1,data2,data3,data4))
    print("                \nДанные сохранены!")
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
