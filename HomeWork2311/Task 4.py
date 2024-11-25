import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(tasks):
    task_id = len(tasks) + 1
    title = input("Введіть назву задачі: ")
    description = input("Введіть опис задачі: ")
    priority = input("Введіть пріоритет (високий/середній/низький): ")
    status = "не виконано"
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": status
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Задача успішно додана!")

def view_tasks(tasks):
    if not tasks:
        print("Список задач порожній.")
        return
    print("\n=== Список задач ===")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Назва: {task['title']}")
        print(f"Опис: {task['description']}")
        print(f"Пріоритет: {task['priority']}")
        print(f"Статус: {task['status']}")
        print("=" * 20)


def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Додати задачу")
        print("2. Переглянути задачі")
        print("3. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
