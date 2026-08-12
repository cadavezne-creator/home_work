import json
import requests # type: ignore

BASE_URL = "http://127.0.0.1:8000/students"
LOG_FILE = "results.txt"


def log_and_print(message):
    """Виводить повідомлення в консоль та записує його у файл."""
    print(message)
    with open(LOG_FILE, mode="a", encoding="utf-8") as f:
        f.write(message + "\n")


def format_response(response):
    """Форматує відповідь від сервера для гарного відображення."""
    try:
        return f"Status Code: {response.status_code}\nResponse JSON: {json.dumps(response.json(), indent=2, ensure_ascii=False)}"
    except ValueError:
        return f"Status Code: {response.status_code}\nResponse Text: {response.text}"


def run_tests():
    # Очищуємо файл результатів перед початком тесту
    open(LOG_FILE, "w", encoding="utf-8").close()

    log_and_print("=== ЗАПУСК ТЕСТУВАННЯ REST API ===\n")

    # 1. Отримати всіх наявних студентів (GET)
    log_and_print("--- Крок 1: Отримати всіх наявних студентів (GET) ---")
    res = requests.get(BASE_URL)
    log_and_print(format_response(res) + "\n")

    # 2. Створити трьох студентів (POST)
    log_and_print("--- Крок 2: Створити трьох студентів (POST) ---")
    students_to_create = [
        {"id": 101, "first_name": "Олег", "last_name": "Лисенко", "age": 19},
        {"id": 102, "first_name": "Анна", "last_name": "Шевченко", "age": 20},
        {"id": 103, "first_name": "Дмитро", "last_name": "Бондар", "age": 21},
    ]

    for student in students_to_create:
        log_and_print(f"Додавання студента ID {student['id']}...")
        res = requests.post(BASE_URL, json=student)
        log_and_print(format_response(res) + "\n")

    # 3. Отримати інформацію про всіх наявних студентів (GET)
    log_and_print(
        "--- Крок 3: Отримати інформацію про всіх наявних студентів (GET) ---"
    )
    res = requests.get(BASE_URL)
    log_and_print(format_response(res) + "\n")

    # 4. Оновити вік другого студента (PATCH)
    log_and_print("--- Крок 4: Оновити вік другого студента ID 102 (PATCH) ---")
    res = requests.patch(f"{BASE_URL}/102", json={"age": 25})
    log_and_print(format_response(res) + "\n")

    # 5. Отримати інформацію про другого студента (GET)
    log_and_print("--- Крок 5: Отримати інформацію про другого студента (GET) ---")
    res = requests.get(f"{BASE_URL}/102")
    log_and_print(format_response(res) + "\n")

    # 6. Оновити імʼя, прізвище та вік处理 третього студента (PUT)
    log_and_print(
        "--- Крок 6: Повне оновлення даних третього студента ID 103 (PUT) ---"
    )
    updated_data = {"first_name": "Данило", "last_name": "Ткаченко", "age": 22}
    res = requests.put(f"{BASE_URL}/103", json=updated_data)
    log_and_print(format_response(res) + "\n")

    # 7. Отримати інформацію про третього студента (GET)
    log_and_print("--- Крок 7: Отримати інформацію про третього студента (GET) ---")
    res = requests.get(f"{BASE_URL}/103")
    log_and_print(format_response(res) + "\n")

    # 8. Отримати всіх наявних студентів (GET)
    log_and_print("--- Крок 8: Отримати всіх наявних студентів (GET) ---")
    res = requests.get(BASE_URL)
    log_and_print(format_response(res) + "\n")

    # 9. Видалити першого користувача (DELETE)
    log_and_print(
        "--- Крок 9: Видалити першого створеного користувача ID 101 (DELETE) ---"
    )
    res = requests.delete(f"{BASE_URL}/101")
    log_and_print(format_response(res) + "\n")

    # 10. Отримати всіх наявних студентів (GET)
    log_and_print(
        "--- Крок 10: Отримати всіх наявних студентів після видалення (GET) ---"
    )
    res = requests.get(BASE_URL)
    log_and_print(format_response(res) + "\n")

    log_and_print("=== ТЕСТУВАННЯ ЗАВЕРШЕНО. Результати збережено в results.txt ===")


if __name__ == "__main__":
    run_tests()
