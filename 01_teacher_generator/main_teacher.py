import file as f
import date_from_calendar as dat_cal
import students as stud


def generate_mails(s_dict):
    with open("mail.txt", 'r') as mail:
        print(mail.readlines())


def main():
    print(f"""\033[1m \nYour file should have the following structure:\033[0m
        \033[1m student_id\033[0m -> int
        \033[1m class_nr\033[0m -> str
        \033[1m name\033[0m -> str
        \033[1m surname\033[0m -> str
        \033[1m missing_tasks\033[0m -> int
        \033[1m grade\033[0m -> float
          """)
    file_path = f.check_if_file_correct()
    stud_dict = stud.add_students_to_dict(file_path)
    print(stud_dict)
    date = dat_cal.due_date()
    generate_mails(stud_dict)

    with open("mail.txt", 'r') as mail:
        print(mail.readlines())


if __name__ == '__main__':
    main()
