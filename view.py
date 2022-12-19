def info_for_search():
    return input('Введите информацию для поиска: ')

def work_mode():
    return input('Введите режим работы ( 1 добавление, 2 поиск): ')

def info_people():
    name = input('Введите имя: ')
    mob_phone = input('Введите номер мобильного телефона: ')
    return f'{name}: {mob_phone}'

def search_result(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)
        