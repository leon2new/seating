import random

# Чтение параметров рассадки из settings.txt
def read_settings(file_path):
    settings = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            settings[key] = value
    return settings

# Чтение информации о школьниках из students.txt
def read_students(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            student_id = int(parts[0])
            student_name = parts[1]
            student_personality = parts[2]
            student_status = int(parts[3])
            students.append((student_id, student_name, student_personality, student_status))
    return students

# Рассадка школьников
def assign_seats(rows, columns, students, seating_plan_file):
    random.shuffle(students)
    seating_plan = [['' for _ in range(columns)] for _ in range(rows)]

    def is_compatible(personality1, personality2, status1, status2):
        # Функция для проверки совместимости характеров и статусов школьников
        return (personality1 == 'active' and personality2 == 'quiet') or \
               (personality1 == 'quiet' and personality2 == 'active') or \
               (status1 == 0 or status2 == 0)

    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if not is_compatible(students[i][2], students[j][2], students[i][3], students[j][3]):
                students[i], students[j] = students[j], students[i]

    current_row = 0
    current_col = 0

    for student_id, student_name, _, _ in students:
        seating_plan[current_row][current_col] = f"{student_id}: {student_name}"
        current_col += 1
        if current_col == columns:
            current_col = 0
            current_row += 1

    # Запись рассадки в seating_plan.txt
    with open(seating_plan_file, 'w') as file:
        for row in seating_plan:
            file.write(','.join(row) + '\n')

if __name__ == "__main__":
    settings = read_settings("settings.txt")
    students = read_students("students.txt")
    rows = int(settings['rows'])
    columns = int(settings['columns'])
    seating_plan_file = "seating_plan.txt"

    assign_seats(rows, columns, students, seating_plan_file)
    print("Рассадка завершена. Результат записан в seating_plan.txt.")
