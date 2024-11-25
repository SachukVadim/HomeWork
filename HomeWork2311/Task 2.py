import shelve


def save_link(short_name, full_url):
    with shelve.open("links_db") as db:
        if short_name in db:
            print("Ця коротка назва вже існує. Спробуйте іншу.")
        else:
            db[short_name] = full_url
            print(f"Посилання '{full_url}' збережено як '{short_name}'.")


def get_link(short_name):
    with shelve.open("links_db") as db:
        if short_name in db:
            print(f"Початкове посилання: {db[short_name]}")
        else:
            print("Такого короткого імені немає в базі даних.")


def main():
    while True:
        print("\n=== Сервіс скорочення посилань ===")
        print("1. Додати посилання")
        print("2. Отримати посилання")
        print("3. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            full_url = input("Введіть повне посилання: ")
            short_name = input("Введіть коротку назву: ")
            save_link(short_name, full_url)
        elif choice == "2":
            short_name = input("Введіть коротку назву: ")
            get_link(short_name)
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
