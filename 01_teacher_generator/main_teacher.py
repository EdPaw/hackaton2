import file as f
import students as stud
import mails as mail
import date_from_calendar as dat_cal


def ask_for_total_tasks():
    valid_input = False

    while not valid_input:
        try:
            total_tasks = int(input("How many tasks were there in total? -> "))
            valid_input = True
            return total_tasks
        except ValueError:
            print("Invalid input. Please enter a valid integer number for the total tasks.")


def main():
    print(f"""\033[1m \nYour file should have the following structure:\033[0m
        \033[1m student_id\033[0m -> int
        \033[1m class_nr\033[0m -> str
        \033[1m name\033[0m -> str
        \033[1m surname\033[0m -> str
        \033[1m missing_tasks\033[0m -> int
        \033[1m grade\033[0m -> float or str 'absent'
          """)

    file_path = f.check_if_file_correct()
    stud_dict = stud.add_students_to_dict(file_path)
    selected_date = dat_cal.due_date()
    total_tasks = ask_for_total_tasks()

    mail.generate_mails(stud_dict, selected_date, total_tasks)


if __name__ == '__main__':
    main()
