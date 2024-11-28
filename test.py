# Загрузка книг из файла
# Сохранение файла
# Добавление книги
# Удаление книги
# Поиск книги
# Отображение всех книг
# Изменение статуса книги


# Добавление книги

# импортируем основные библиотеки
import os
import json

# проверим наличие файла, если он отсутствует - создадим
base = "library_base.json"
if not os.path.exists(base):
    with open(base, 'w', encoding='utf-8') as f:
        json.dump([], f)


# Загрузка книг из файла
def load_base():
    with open(base, 'r', encoding='utf-8') as f:
        return json.load(f)


# Сохранение в файл
def save_base(list_books):
    with open(base, 'w', encoding='utf-8') as f:
        json.dump(list_books, f, indent=4, ensure_ascii=False)


# Добавление книги
def add_book(title, author, year):
    list_books = load_base()

    if not (1500 <= year < 2100):
        print("Ошибка: Год издания должен быть в диапазоне от 1500 до 2099.")
        return
    if not isinstance(title, str) or not isinstance(author, str) or not title.strip() or not author.strip():
        print("Ошибка: Название книги и автор должны быть непустыми строками.")
        return

    if list_books:
        list_books_id = max([book["id"] for book in list_books]) + 1
    else:
        list_books_id = 1
    list_books.append(
        {'id': list_books_id, 'title': title.strip(), 'author': author.strip(), 'year': year, 'status': 'в наличии'})
    save_base(list_books)
    print("Книга добавлена")


# Удаление книги
def delete_book(id_book):
    try:
        id_book = int(id_book)  # Преобразуем ввод в число
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    list_books = load_base()  # Загружаем базу

    # Проверим, существует ли книга с указанным ID
    book_exists = any(book['id'] == id_book for book in list_books)
    if not book_exists:
        print(f"Ошибка: Книга с ID {id_book} не найдена!")
        return

    # Удаляем книгу
    list_books = [book for book in list_books if book['id'] != id_book]
    save_base(list_books)
    print(f"Книга с ID {id_book} успешно удалена.")


# Поиск книги
def search_book(key_id):
    list_books = load_base()  # Загружаем базу

    try:
        key_id = key_id.strip().lower()
        books = []
        key_id_params = input(f"Введите значение для поиска по '{key_id}': ")

        # Проверим, что хотя бы одно значение введено
        if not key_id_params:
            print("Значение не введено!")
            return

        # Поиск книг по введенным столбцам
        if key_id == "title":
            for book in list_books:
                if book[key_id] == key_id_params:
                    books.append(book)
            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "author":
            for book in list_books:
                if book[key_id] == key_id_params:
                    books.append(book)
            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "year":
            for book in list_books:
                if book[key_id] == key_id_params:
                    books.append(book)
            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "title|author":
            key_id_title = input(f"Введите значение для поиска по 'title': ").strip()
            key_id_author = input(f"Введите значение для поиска по 'author': ").strip()
            key_id = key_id.strip().split('|')

            # Проверим, что хотя бы одно значение введено
            if not key_id_title and not key_id_author:
                print("Оба значения для поиска пусты!")
                return

            books = []
            for book in list_books:
                if (book[key_id[0]] == key_id_title) or (book[key_id[1]] == key_id_author):
                    books.append(book)

            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "title|year":
            key_id_title = input(f"Введите значение для поиска по 'title': ").strip()
            key_id_year = input(f"Введите значение для поиска по 'year': ").strip()
            key_id = key_id.strip().split('|')

            # Проверим, что хотя бы одно значение введено
            if not key_id_title and not key_id_year:
                print("Оба значения для поиска пусты!")
                return

            books = []
            for book in list_books:
                if (book[key_id[0]] == key_id_title) or (book[key_id[1]] == key_id_year):
                    books.append(book)

            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "author|year":
            key_id_author = input(f"Введите значение для поиска по 'title': ").strip()
            key_id_year = input(f"Введите значение для поиска по 'year': ").strip()
            key_id = key_id.strip().split('|')

            # Проверим, что хотя бы одно значение введено
            if not key_id_author and not key_id_year:
                print("Оба значения для поиска пусты!")
                return

            books = []
            for book in list_books:
                if (book[key_id[0]] == key_id_author) or (book[key_id[1]] == key_id_year):
                    books.append(book)

            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

        elif key_id == "title|author|year":
            key_id_title = input(f"Введите значение для поиска по 'title': ").strip()
            key_id_author = input(f"Введите значение для поиска по 'title': ").strip()
            key_id_year = input(f"Введите значение для поиска по 'year': ").strip()
            key_id = key_id.strip().split('|')

            # Проверим, что хотя бы одно значение введено
            if not key_id_author and not key_id_year and not key_id_title:
                print("Не введено ни одно значение!")
                return

            books = []  # список для заполнения найденными книгами
            for book in list_books:
                if (book[key_id[0]] == key_id_author) or (book[key_id[1]] == key_id_year) or (
                        book[key_id[2]] == key_id_title):
                    books.append(book)

            if len(books) > 0:
                print(f"Книга(и) найдена(ы): {books}")
            else:
                print(f"Книга(и) НЕ найдена(ы)!")

    except ValueError:
        print("Ошибка: Некорректное значение!")


# Отображение всех книг
def display_books():
    list_books = load_base()
    # Проверим наличие книг в базе
    if not list_books:
        print("База данных пуста!")
        return
    print("Список всех книг:")

    for book in list_books:
        print(
            f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")


# Изменение статуса книги
def update_status(book_id, status):
    list_books = load_base()
    if len(list_books) != 0:
        for book in list_books:
            # Проверим, что статус книги отличается от требуемого.
            if (book['id'] == book_id) and (book['status'] == status):
                print(f"Статус книги с ID: {book_id} не изменена!")
                return
            else:
                book['status'] = status
                save_base(list_books)
                print(f"Статус книги с ID: {book_id} успешно изменена на {book['status']}")
                return
    else:
        print("Извините, база книг пуста!")


def main():
    # ВЫБЕРИТЕ ОДНО ИЗ ДЕЙСТВИЙ (ЦИФРУ):
    # Загрузка книг из файла
    # Сохранение файла
    # 1. Добавление книги
    # 2. Удаление книги
    # 3. Поиск книги
    # 4. Отображение всех книг
    # 5. Изменение статуса книги
    print(
        f'ВЫБЕРИТЕ ОДНО ИЗ ДЕЙСТВИЙ (ЦИФРУ): \n 1. Добавление книги; \n 2. Удаление книги; \n 3. Поиск книги; \n 4. Отображение всех книг; \n 5. Изменение статуса книги')
    while True:
        try:
            choice = int(input("Введите номер выбранного раздела: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите число от 1 до 6.")
            continue

        match choice:
            case 1:
                print("\nВы вошли в раздел добавления книг. Пожалуйста, введите автора, название книги и год издания.")

                try:
                    load_base()
                    title = str(input("Введите название книги: "))
                    author = str(input("Введите автора книги: "))
                    year = int(input("Введите год издания книги в числовом формате от 1500 до 2099): "))
                    add_book(title, author, year)

                except ValueError:
                    print("Ошибка: Год издания должен быть в числовом формате и в заданном диапазоне")

            case 2:
                print("\nВы вошли в раздел удаления книг. Пожалуйста, введите id книги для удаления.")
                id_book = input("Введите ID книги для удаления: ").strip()  # Считываем как строку, затем преобразуем
                delete_book(id_book)
            case 3:
                print("\nВы вошли в раздел поиска книг.")
                print("По каким параметрам будем искать книгу? title|author|year"
                      "\nВ таком формате: например, year или title|year или author|year. Без пробелов.")
                key_id = input("Введите параметры для поиска: ")
                search_book(key_id)
            case 4:
                print("\nВы вошли в раздел отображения всех книг.")
                display_books()
            case 5:
                print("\nВы вошли в раздел изменения статуса книги.")
                book_id = int(input("Введите числовое значение ID книги: ").strip())
                book_x = []  # список для книг, которые в наличии
                for book in load_base():
                    if book_id == book['id']:
                        print(f"Текущий статус книги.\n ID: {book_id}, Статус: {book['status']} ")
                        status = str(input("Введите новый статус книги (в наличии/выдана): ").lower().strip())
                        book_x.append(book)
                        if status in ["в наличии", "выдана"]:
                            update_status(book_id, status)

                        else:
                            print("Вы ввели некорректный статус")
                if len(book_x) == 0:
                    print(f"Извините, книги с ID: {book_id} нет в нашей базе!")


main()
