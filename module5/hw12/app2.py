import csv
import os
from flask import Flask, jsonify, request

app = Flask (__name__)
CSV_FILE = "students.csv"
FIELDNAMES = ["id", "first_name", "last_name", "age"]

def init_csv():
    """Створює файл CSV з заголовками, якщо він не існує або порожній."""
    file_exists = os.path.exists(CSV_FILE)
    is_empty = file_exists and os.path.getsize(CSV_FILE) == 0
    
    if not file_exists or is_empty:
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def read_students():
    """Безпечно читає всіх студентів з файлу CSV."""
    init_csv()
    students = []
    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Пропускаємо порожні або пошкоджені рядки
                if not row or not row.get("id"):
                    continue
                try:
                    students.append({
                        "id": int(row["id"]),
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "age": int(row["age"])
                    })
                except (ValueError, TypeError) as e:
                    print(f"Помилка конвертації рядка: {row} -> {e}")
                    continue
    except Exception as e:
        print(f"Критична помилка читання файлу: {e}")
    return students

def write_students(students):
    """Записує список студентів у файл CSV."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for s in students:
            writer.writerow({
                "id": s["id"],
                "first_name": s["first_name"],
                "last_name": s["last_name"],
                "age": s["age"]
            })

@app.route('/students', methods=['GET'])
def get_students():
    """Отримання списку всіх студентів."""
    try:
        data = read_students()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json() or {}
    if not all(k in data for k in FIELDNAMES):
        return jsonify({"error": "Missing required fields"}), 400
    
    students = read_students()
    if any(s['id'] == int(data['id']) for s in students):
        return jsonify({"error": "Student with this ID already exists"}), 400

    try:
        new_student = {
            "id": int(data['id']),
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "age": int(data['age'])
        }
        students.append(new_student)
        write_students(students)
        return jsonify(new_student), 201
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid data types. ID and Age must be integers"}), 400

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_put(student_id):
    data = request.get_json() or {}
    if not all(k in data for k in ["first_name", "last_name", "age"]):
        return jsonify({"error": "Missing required fields for PUT"}), 400

    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    try:
        student['first_name'] = data['first_name']
        student['last_name'] = data['last_name']
        student['age'] = int(data['age'])
        write_students(students)
        return jsonify(student), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be an integer"}), 400

@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student_patch(student_id):
    data = request.get_json() or {}
    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    if 'first_name' in data: student['first_name'] = data['first_name']
    if 'last_name' in data: student['last_name'] = data['last_name']
    if 'age' in data:
        try:
            student['age'] = int(data['age'])
        except (ValueError, TypeError):
            return jsonify({"error": "Age must be an integer"}), 400

    write_students(students)
    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if s['id'] != student_id]
    write_students(students)
    return jsonify({"message": f"Student with ID {student_id} deleted"}), 200

@app.route("/", methods=["GET"])
def home():
    """Головна сторінка з підказкою."""
    return (
        jsonify(
            {
                "message": "Welcome to Students REST API!",
                "endpoints": {
                    "get_all_students": "/students (GET)",
                    "get_student_by_id": "/students/<id> (GET)",
                    "create_student": "/students (POST)",
                    "update_student_full": "/students/<id> (PUT)",
                    "update_student_partial": "/students/<id> (PATCH)",
                    "delete_student": "/students/<id> (DELETE)",
                },
            }
        ),
        200,
    )

if __name__ == '__main__':
    app.run(debug=True)