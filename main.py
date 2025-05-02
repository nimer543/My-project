import json
# Функции для работы с JSON
def save_tasks_to_file(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    # Задача: Создать программу для управления задачами с возможностью добавления, редактирования, удаления и фильтрации задач по приоритету.
# Основная программа
menu = 0
tasks = load_tasks_from_file()  # Загружаем задачи из файла при запуске программы
while menu < 6:
    print('\nМеню:')
    print('1. Добавить задачу')
    print('2. Просмотреть задачи')
    print('3. Редактировать задачу')
    print('4. Удалить задачу')
    print('5. Фильтровать задачи по приоритету')
    print('6. Выход\n')
    menu = int(input('Выберите пункт меню (1-6):\n'))
    # Раздел добавления задачи
    if menu == 1:
        name = input('Введите название задачи:')
        description = input('Введите описание задачи:')
        priority = input('Введите приоритет задачи (высокий, средний, низкий):') 
        print('Задача добавлена!')
        tasks.append(
            {'Название': name, 'Описание': description, 'Приоритет': priority }
        )
        save_tasks_to_file(tasks)  # Сохраняем задачи в файл
        menu = int(input('6. Выход\n'
        '0. Продолжить\n'
        'Выберите пункт меню (0 или 6):\n'))
    elif menu == 2:
        if  not tasks:
            print('Список задач пуст\n')
        for i,task in enumerate(tasks[:],start=1):
               print(f"\n{i}. Название: {task['Название']}, Описание: {task['Описание']}, Приоритет: {task['Приоритет']}\n")
        menu = int(input('6. Выход\n'
        '0. Продолжить\n'
        'Выберите пункт меню (0 или 6):\n'))
    elif menu == 3:
        for i,task in enumerate(tasks[:],start=1):
            print(f"\n{i}. Название: {task.get('Название', 'Нет названия')}, Описание: {task.get('Описание', 'Нет описания')}, Приоритет: {task.get('Приоритет', 'Нет приоритета')}\n")
        dictionary_num = int(input("Укажите номер задачи которую вы хоите редактировать?\n"))-1
        if 0 <= dictionary_num < len(tasks):
            chosen_dict = tasks[dictionary_num]
            for i, task in enumerate(tasks):
                task['Индекс'] = i
            nav = int(input('Выберите что вы хотите изменить\n'
                            '1. Название\n'
                            '2. Описание\n'
                            '3. Приоритет\n'))-1
            keys = ['Название', 'Описание', 'Приоритет']  # Список ключей
            if 0 <= nav < len(keys):  # Проверяем, что nav в допустимом диапазоне
                new_value = input(f'Введите новое значение для {keys[nav]}: ')
                tasks[dictionary_num][keys[nav]] = new_value  # Обновляем значение в словаре
                save_tasks_to_file(tasks)  # Сохраняем изменения в файл
                print('Задача обновлена!\n')
            else:  
                print('Некорректный выбор.\n')  
                break    
        menu = int(input('6. Выход\n'
        '0. Продолжить\n'
        'Выберите пункт меню (0 или 6):\n'))
    if menu == 4:
        for i,task in enumerate(tasks[:],start=1):
            print(f"\n{i}. Название: {task.get('Название', 'Нет названия')}, Описание: {task.get('Описание', 'Нет описания')}, Приоритет: {task.get('Приоритет', 'Нет приоритета')}\n")
        dictionary_num = int(input("Укажите номер задачи которую вы хоите Удалить?\n"))-1
        if 0 <= dictionary_num < len(tasks):
            chosen_dict = tasks[dictionary_num]
            for i, task in enumerate(tasks):
                    task['Индекс'] = i
            nav = int(input('Выберите что вы хотите удалить\n'
                            '1. Название\n'
                            '2. Описание\n'
                            '3. Приоритет\n'
                            '4. Удалить всю задачу\n'))-1
            keys = ['Название', 'Описание', 'Приоритет']
            if 0 <= nav < len(keys) and nav != 3:
                tasks[dictionary_num][keys[nav]] = ""
                save_tasks_to_file(tasks)
                print(f'Значение для "{keys[nav]}" удалено!\n')
            elif nav == 3:
               del tasks[dictionary_num]
               save_tasks_to_file(tasks)
               print('Задача удалена\n')
            else:  
                print('Некорректный выбор.\n')      
        menu = int(input('6. Выход\n'
            '0. Продолжить\n'
            'Выберите пункт меню (0 или 6):\n'))
    if menu == 5:
        nav = int(input('\nВыберите какой приоритет хотите увидеть\n'
                        '1. Низкий приоритет\n'
                        '2. Средний приоритет\n'
                        '3. Высокий приоритет\n'))-1
        priority_levels = ['низкий','средний','высокий']
        if 0 <= nav < len(priority_levels):
             selected_priority = priority_levels[nav]  # Выбранный приоритет
             filtered_tasks = [task for task in tasks if task['Приоритет'].lower() == selected_priority]  # Фильтруем задачи
             if filtered_tasks:
                print('Задачи с выбранным приоритетом:')
                for i, task in enumerate(filtered_tasks, start=1):
                        print(f"{i}. Название: {task['Название']}, Описание: {task['Описание']}, Приоритет: {task['Приоритет']}\n")
             else:
                 print('Нет задач с выбранным приоритетом.\n')
        else:
            print('Некорректный выбор.\n')
           
        menu = int(input('6. Выход\n'
            '0. Продолжить\n'
            'Выберите пункт меню (0 или 6):\n'))