def potential_grade(missing_tasks, current_grade, total_tasks):
    return str(current_grade + (round(6/int(total_tasks)) * missing_tasks/2))


def generate_mails(dicty, due_date, total_tasks):

    success = 0

    with open("mail.txt", 'r') as mail:
        template = mail.read()

        for key, value in dicty.items():
            result = template.replace("[insert student name]", str(value[1]))
            result = result.replace("[insert number of missing tasks]", str(value[3]))
            result = result.replace("[insert current grade]", str(value[4]))
            result = result.replace("[insert potential grade]", potential_grade(value[3], value[4], total_tasks))
            result = result.replace("[insert one date for all students]", due_date)

            try:
                with open(f"mail_{key}_{str(value[1])}_{str(value[2])}.txt", 'x') as output_file:
                    output_file.write(result)
                    success = 1
            except FileExistsError as e:
                success = 0

    if success == 1:
        print("Success. Files generated.")
    else:
        print("This filename already exists. Please check your files and try again.")
