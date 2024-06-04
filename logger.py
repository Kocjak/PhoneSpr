from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n" 
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('\nВывожу данные из 1 файла: \n')
    with open('data_first_variant.csv','r',encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list=[]
        j = 0

        for i in range(len(data_first)):
            if data_first[i] ==  '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))

    print('\nВывожу данные из 2 файла: \n')
    with open('data_second_variant.csv','r',encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def delete_data():

    
    str = []
    var = int(input(f"\nВ каком файле необходимо удалить запись?\n" 
                f"Выберите вариант: "))

    if var == 1:
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            str = f.readlines()
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            for i, line in enumerate(f): print(i+1, line)
            print("Какую строку удаляем?")
            str_num = int(input('Введите номер строки: '))
        with open('data_first_variant.csv','w',encoding='utf-8') as f:
            for i, line in enumerate(str):
                if i not in [str_num-1]:
                    f.write(line)         

    elif var == 2:
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            str = f.readlines()
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            for i, line in enumerate(f): print(i+1, line)
            print("Какую строку удаляем?")
            str_num = int(input('Введите номер строки: '))
        with open('data_second_variant.csv','w',encoding='utf-8') as f:
            for i, line in enumerate(str):
                if i not in [str_num-1]:
                    f.write(line)


def replace_data():

    var = int(input(f"\nВ каком файле необходимо заменить запись?\n" 
                f"Выберите вариант: "))
    
    if var == 1:
        old_text = input(f"\nКакое значение нужно заменить?\n" 
                f"Введите значение: ")
        
        new_text = input(f"\nНа какое нужно заменить?\n" 
                f"Введите значение: ")
        
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            str = f.read()
            str = str.replace(old_text, new_text)
        
        with open('data_first_variant.csv','w',encoding='utf-8') as f:
            f.write(str)

    elif var == 2:
        old_text = input(f"\nКакое значение нужно заменить?\n" 
                f"Введите значение: ")
        
        new_text = input(f"\nНа какое нужно заменить?\n" 
                f"Введите значение: ")
        
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            str = f.read()
            str = str.replace(old_text, new_text)
        
        with open('data_second_variant.csv','w',encoding='utf-8') as f:
            f.write(str)
        
