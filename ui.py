from logger import input_data, print_data, delete_data,replace_data

def interface():
    print("Добрый день! Вы попали на специальный бот от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление записи \n 4 - замена записи")
    command = int(input('Введите число '))

    while command !=1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command==1:
        input_data()
    elif command ==2:
        print_data()
    elif command ==3:
        delete_data()
    elif command ==4:
        replace_data()