import csv
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
CSV_FILE = "students.csv"
FIELDNAMES = ["id", "first_name", "last_name", "age"]


def init_csv():
    """Створює CSV-файл із заголовками, якщо він не існує."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_students():
    """Читає всіх студентів із CSV-файлу."""
    init_csv()
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_students(students):
    """Перезаписує CSV-файл оновленим списком студентів."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


# GET /students - Отримати список усіх студентів
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(read_students()), 200


# GET /students/<id> - Отримати студента за ID
@app.route("/students/<string:student_id>", methods=["GET"])
def get_student(student_id):
    students = read_students()
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


# POST /students - Додати нового студента
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json() or {}

    # Перевірка обов'язкових полів
    required_fields = ["id", "first_name", "last_name", "age"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    students = read_students()

    # Перевірка на унікальність ID
    if any(s["id"] == str(data["id"]) for s in students):
        return jsonify({"error": "Student with this ID already exists"}), 400

    new_student = {
        "id": str(data["id"]),
        "first_name": str(data["first_name"]),
        "last_name": str(data["last_name"]),
        "age": str(data["age"]),
    }

    students.append(new_student)
    write_students(students)
    return jsonify(new_student), 201


# PUT /students/<id> - Повне оновлення даних студента
@app.route("/students/<string:student_id>", methods=["PUT"])
def update_student_put(student_id):
    data = request.get_json() or {}
    required_fields = ["first_name", "last_name", "age"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields for full update"}), 400

    students = read_students()
    student_index = next(
        (i for i, s in enumerate(students) if s["id"] == student_id), None
    )

    if student_index is None:
        return jsonify({"error": "Student not found"}), 404

    students[student_index] = {
        "id": student_id,
        "first_name": str(data["first_name"]),
        "last_name": str(data["last_name"]),
        "age": str(data["age"]),
    }

    write_students(students)
    return jsonify(students[student_index]), 200


# PATCH /students/<id> - Часткове оновлення даних студента
@app.route("/students/<string:student_id>", methods=["PATCH"])
def update_student_patch(student_id):
    data = request.get_json() or {}
    students = read_students()
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    # Оновлюємо лише ті поля, які передані в запиті
    if "first_name" in data:
        student["first_name"] = str(data["first_name"])
    if "last_name" in data:
        student["last_name"] = str(data["last_name"])
    if "age" in data:
        student["age"] = str(data["age"])

    write_students(students)
    return jsonify(student), 200


# DELETE /students/<id> - Видалення студента
@app.route("/students/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
    students = read_students()
    updated_students = [s for s in students if s["id"] != student_id]

    if len(students) == len(updated_students):
        return jsonify({"error": "Student not found"}), 404

    write_students(updated_students)
    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == "__main__":
    init_csv()
    app.run(debug=True)

