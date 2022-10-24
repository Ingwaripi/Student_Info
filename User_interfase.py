import logging as log
import view_data as vd
import search as sea



print("\n     Добро пожаловать в студенческуя библиотеку, выбери опцию для работы!")

def result_opt():
    print('''
    1 - Внести данные
    2 - Посмотреть данные
    3 - Найти студента
    ''')
    result = int(input("Выбирите операцию: "))
    if result == 1:
        data1 = vd.get_name()
        data2 = vd.get_sernamr()
        data3 = vd.get_date_of_birth()
        data4 = vd.get_data_group()
        log.loger_stud(data1,data2,data3,data4)
        return log.again()
        
    if result == 2:
        return sea.see_data(), sea.again()
        
    if result == 3:
        return sea.search_students(), sea.again()
    