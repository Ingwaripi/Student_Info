import User_interfase as ui


def get_name():
    result_name = input('Введите имя:').lower()
    return result_name
def get_sernamr():
    result_sername = input('Ведите фамилию:').lower()
    return result_sername
def get_date_of_birth():
    result_date_of_birth = input("введите дату рождения через пробел: ")
    var = str(result_date_of_birth).replace(" ",".")
    return var

def get_data_group():
    result_group = input("Введите номер группы: ")
    return result_group
    
