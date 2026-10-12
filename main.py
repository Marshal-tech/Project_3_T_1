def print_students(students):
    for i in students:
        print("Оцінки", i, "-", students[i])


def add_student(students):
    key = input("Введіть прізвище та ім'я учня: ")
    try:
        grades_str = input("Введіть 10 оцінок через пробіл: ")
        grades = [int(x) for x in grades_str.split()]
        students[key] = grades
        print("Додано", key, ".")
    except ValueError:
        print("Помилка: оцінки повинні бути числами!")


def del_student(students):
    key = input("Введіть прізвище та ім'я для видалення: ")
    try:
        del students[key]
        print("Видалено", key, ".")
    except KeyError:
        print(f"Помилка: Учня з ім'ям '{key}' не знайдено у словнику!")


def print_sort(students):
    sorted_students = {k: students[k] for k in sorted(students)}
    print("Відсортований словник:")
    for i in sorted_students:
        print("Оцінки", i, "-", sorted_students[i])


def find_max_sum(students):
    if not students:
        print("Словник порожній!")
        return

    best_student = max(students, key=lambda k: sum(students[k]))
    max_sum = sum(students[best_student])
    print(f"Учень з найбільшою сумою оцінок: {best_student}. Сума: {max_sum}")


def find_min_sum(students):
    if not students:
        print("Словник порожній!")
        return

    worst_student = min(students, key=lambda k: sum(students[k]))
    min_sum = sum(students[worst_student])
    print(f"Учень з найменшою сумою оцінок: {worst_student}. Сума: {min_sum}")


def main():
    students = {
        "Vitaly_Prykhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10],
        "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
        "Mykhailo_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4],
        "Maxim_Deryzemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7],
        "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12],
        "Andriy_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8],
        "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10],
        "Ivan_Petrov": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        "Olena_Sydorenko": [11, 11, 10, 10, 12, 12, 11, 10, 11, 12],
        "Taras_Shevchenko": [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    }

    while True:
        print("\n" + "-" * 80)
        print("Якщо ви бажаєте виведення усіх значень словника, тоді натисніть -> 1 <-")
        print("Якщо ви бажаєте добавити новий запис до словника, тоді натисніть -> 2 <-")
        print("Якщо ви бажаєте видалення запису із словника, тоді натисніть -> 3 <-")
        print("Якщо ви бажаєте перегляд вмісту словника за відсортованими ключами, тоді натисніть -> 4 <-")
        print("Якщо ви бажаєте визначити прізвище та ім'я учня, який має найбільшу суму оцінок, тоді натисніть -> 5 <-")
        print("Якщо ви бажаєте визначити прізвище та ім'я учня, який має найменшу суму оцінок, тоді натисніть -> 6 <-")
        print("Якщо ви бажаєте вийти з програми, тоді натисніть -> 0 <-")
        print("-" * 80)

        choice = input("Введіть пункт меню: ")

        if choice == '1':
            print_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            del_student(students)
        elif choice == '4':
            print_sort(students)
        elif choice == '5':
            find_max_sum(students)
        elif choice == '6':
            find_min_sum(students)
        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірне значення, оберіть цифру від 0 до 6.")


if __name__ == "__main__":
    main()