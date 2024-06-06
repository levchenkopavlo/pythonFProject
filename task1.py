import random

# 1. Напишіть програму, яка приймає два цілих числа від користувача і виводить суму діапазону чисел між ними.
# while True:
#     try:
#         number1 = int(input('input number1: '))
#         number2 = int(input('input number2: '))
#         break
#     except ValueError:
#         print('Input error')
#         continue
# if number1 > number2:
#     number1, number2 = number2, number1
# summ = 0
# for number in range(number1, number2 + 1):
#     summ += number
#
# # summ = sum(range(number1, number2 + 1))
# print(f'sum of digits: {summ}')

# 2. Напишіть програму, для знаходження суми всіх парних чисел від 1 до 100.
limit1 = 1
limit2 = 100
summ_even = 0
for number in range(limit1, limit2 + 1):
    if not number % 2:
        summ_even += number
print(f'суми всіх парних чисел в діапазоні: {summ_even}')

# 3. Напишіть програму, яка приймає рядок від користувача і виводить кожну літеру рядка на окремому рядку.
# line = input('Введіть рядок: ')
# for char in line:
#     print(char)

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
# string_list = []
# result_list = []
# while True:
#     line = input('Введіть рядок тексту (Enter для виходу): ')
#     if line == '':
#         break
#     else:
#         string_list.append(line)
# print(string_list)
# for line in string_list:
#     if line[0].isupper():
#         result_list.append(line)
# print(result_list)

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
