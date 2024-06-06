import random

# 1. Напишіть програму, яка приймає два цілих числа від користувача і виводить суму діапазону чисел між ними.
while True:
    try:
        number1 = int(input('input number1: '))
        number2 = int(input('input number2: '))
        break
    except ValueError:
        print('Input error')
        continue
if number1 > number2:
    number1, number2 = number2, number1
summ = 0
for number in range(number1, number2 + 1):
    summ += number

# summ = sum(range(number1, number2 + 1))
print(f'sum of digits: {summ}')

# 2. Напишіть програму, для знаходження суми всіх парних чисел від 1 до 100.
limit1 = 1
limit2 = 100
summ_even = 0
for number in range(limit1, limit2 + 1):
    if not number % 2:
        summ_even += number
print(f'суми всіх парних чисел в діапазоні: {summ_even}')

# 3. Напишіть програму, яка приймає рядок від користувача і виводить кожну літеру рядка на окремому рядку.
line = input('Введіть рядок: ')
for char in line:
    print(char)

# 4. Напишіть програму, яка створює список цілих чисел та виводить новий список, який містить лише парні числа з
# вихідного списку.
size = 5
limit1 = 1
limit2 = 100
random_list = [random.randint(limit1, limit2) for _ in range(size)]
print(f'{random_list = } ')
result_list = [number for number in random_list if not number % 2]
print(f'{result_list = } ')

# 5. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.
string_list = []
result_list = []
while True:
    line = input('Введіть рядок тексту (Enter для виходу): ')
    if line == '':
        break
    else:
        string_list.append(line)
print(string_list)
for line in string_list:
    if line[0].isupper():
        result_list.append(line)
print(result_list)

# 6. Напишіть функцію, яка приймає список рядків від користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
string_list = []
result_list = []
word = 'Python'
while True:
    line = input('Введіть рядок тексту (Enter для виходу): ')
    if line == '':
        break
    else:
        string_list.append(line)
print(string_list)
for line in string_list:
    if word in line:
        result_list.append(line)
print(result_list)

# 7. (додаткове на кристалики)Напишіть програму, яка створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти та шукати слова у цьому словнику.
dictionary = {}

while True:
    print("---------------------------------------------")
    print("Оберіть дію.")
    print("\033[33m1\033[0m. Додати слово")
    print("\033[33m2\033[0m. Видалити слово")
    print("\033[33m3\033[0m. Шукати слово")
    userChoice = input("Ваш вибір (Enter для виходу): ")

    match userChoice:
        case "":
            break
        case "1":
            word = input('Введіть слово: ')
            definition = input('Введіть визначення: ')
            dictionary[word] = definition
        case "2":
            word = input('Введіть слово для видалення: ')
            del dictionary[word]

        case "3":
            search_word = input('Введіть слово (або частину слова) для пошуку: ')
            for word in dictionary:
                if search_word.lower() in word.lower():
                    print(f'{word}: {dictionary[word]}')
        case _:
            continue

# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1, 3), (3, 2), (2, 1)]).

# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті.
import datetime


class WebPage:
    pages = []

    def __init__(self, title, content=None):
        self.title = title
        self.content = content
        self.date = datetime.datetime.now()

    def page_info(self):
        print(f'\tНазва сторінки: {self.title}')
        print(f'\tДата створення: {self.date}')


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)
        print(f'Сторінку {page.title} додано.')

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print(f'Сторінку {page.title} видалено.')
                return
        print(f'Сторінку {title} не знайдено.')

    def show_info(self):
        print(f'Назва сайту: {self.name}')
        print(f'Адреса сайту: {self.url}')
        print(f'Всього сторінок: {len(self.pages)}')
        if len(self.pages):
            for page in self.pages:
                page.page_info()

def site_choice():
    print('Виберіть сайт')
    counter = 1
    for site in websites:
        print(f"\033[33m{counter}\033[0m. {site.name}")
        counter += 1
    while True:
        choise = input('Виберіть сайт: ')
        if 0 < int(choise) <= len(websites):
            return websites[int(choise) - 1]

websites = []
while True:
    print("Оберіть дію.")
    print("\033[33m1\033[0m. Створити новий сайт")
    if websites:
        print("\033[33m2\033[0m. Додати сторінку до сайту")
        print("\033[33m3\033[0m. Видалити сторінку")
        print("\033[33m4\033[0m. Інформація про сайт")
    userChoice = input("Ваш вибір (Enter для виходу): ")

    match userChoice:
        case "":
            break
        case "1":
            site_name = input('Введіть назву сайту: ')
            site_url = input('Введіть адресу сайту: ')
            website = WebSite(site_name, site_url)
            websites.append(website)

        case "2":
            website = site_choice()
            page_title = input('Введіть заголовок сторінки: ')
            page_content = input('Введіть вміст сторінки: ')
            page = WebPage(page_title, page_content)
            website.add_page(page)

        case "3":
            website = site_choice()
            page_title = input('Введіть заголовок сторінки для видалення: ')
            website.remove_page(page_title)

        case "4":
            website = site_choice()
            website.show_info()
        case _:
            continue
