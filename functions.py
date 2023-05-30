
def show_data():
    """Выводит информацию из справочника"""
    with open('sem_8_practice\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data():
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО:')
    phone_num = input('Введите номер телефона: ')
    with open('sem_8_practice\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data():
    """Печатает результат поиска по справочнику."""
    with open('sem_8_practice\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: list, info: str) -> list:
    """Находит в списке записи по определенному критерию поиска"""
    # return [contact for contact in book if info.lower() in contact.lower()]
    data = list(filter(lambda contact: info.lower() in contact.lower(), book))
    for id, val in enumerate(data):
        print(f'{id+1}. {val}')
    if id > 0:
        change_number = int(
            input(f'Выберите номер строки с искомым контактом: от 1 до {id+1}: '))
        return data[change_number-1]
    else:
        return data[id]


def correct_data():
    """Корректирует информацию в справочнике"""
    with open('sem_8_practice\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_find = input('Введите, что хотите найти: ')
    search_for_correct = search(data, contact_to_find)
    print(f'Данные для корректировки\удаления: {search_for_correct}')
    change_of_option = int(input("1 - удаление данных, 2 - корректировка данных: "))
    if change_of_option == 1:
        data.remove(search_for_correct)
    elif change_of_option == 2:
        data[data.index(search_for_correct)] = input('Введите корректные ФИО и номер телефона: ')
    with open('sem_8_practice\\book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))