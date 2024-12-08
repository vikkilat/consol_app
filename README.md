# Консольное приложение "Библиотека"

## Описание
Приложение "Библиотека" предназначено для управления списком книг. Оно позволяет добавлять, удалять и искать книги, а также изменять их статус. Все данные о книгах сохраняются в JSON-файле, что обеспечивает их сохранение между запусками программы.

## Функциональность

- **Добавление книги:**
  - Пользователь вводит название, автора и год издания книги.
  - Проверяется корректность введенных данных.
  - Книга сохраняется в библиотеке с уникальным идентификатором.

- **Удаление книги:**
  - Удаление книги по её идентификатору (ID).

- **Поиск книг:**
  - Возможность поиска книг по названию, автору или году издания.

- **Просмотр всех книг:**
  - Отображение списка всех книг в библиотеке с их полными данными.

- **Изменение статуса книги:**
  - Возможность установить статус книги как "в наличии" или "выдана".

## Технологии

- Python 3.11
- JSON для хранения данных

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/vikkilat/consol_app.git
   ```

2. Перейдите в директорию проекта:
   ```
   cd consol_app
   ```

3. Убедитесь, что у вас установлен Python версии 3.11 или выше.

4. Запустите приложение:
   ```
   python library.py
   ```

## Использование

При запуске программы отобразится меню с возможными действиями:

1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
6. Выход

Для выполнения действия выберите номер пункта меню и следуйте инструкциям в консоли.

## Пример

Пример добавления книги:

```
Меню:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
6. Выход

Выберите действие: 1
Введите название книги: Преступление и наказание
Введите автора книги: Федор Достоевский
Введите год издания книги: 1866
Книга 'Преступление и наказание' добавлена в библиотеку.
```

## Контакты

[Латышева Виктория](https://github.com/vikkilat)
