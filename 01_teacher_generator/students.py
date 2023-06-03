import csv


def add_students_to_dict(file_path):
    students_info = {}

    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)

            for row in reader:
                student_id = int(row[0])
                class_nr = str(row[1])
                name = str(row[2])
                surname = str(row[3])
                missing_tasks = int(row[4])
                grade = float(row[5])

                students_info[student_id] = [class_nr, name, surname, missing_tasks, grade]
    except ValueError as e:
        print(f"\033[3mYour file has wrong structure. Correct it before passing it to this program. {e}\033[0m")

    return students_info
