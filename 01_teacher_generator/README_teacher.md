# Teacher Mail Generator

Program is implementation of 'Teacher Mail Generator'.

How program works:
<br />⮩ The program starts by displaying the required structure of the input file. It prompts the user to provide the file path, 
verifies its correctness, and proceeds to extract the student information into a dictionary.
<br />⮩ Next, the program allows the user to select a due date using a date selector. The selected date is stored for later use.
<br />⮩ The program then prompts the user to enter the total number of tasks. This information is required to calculate potential grade.
<br />⮩ Using the student dictionary, selected due date and total tasks, the program generates individualized emails for each student.
<br />⮩ The emails are saved as separate files in the .txt format (if files do not already exist).

<br />⮩ Note: The program uses special formatting for displaying the required structure and highlighting certain text in the console output.

Modules:
<br />⮩ file
<br />⮩ date_from_calendar
<br />⮩ students
<br />⮩ mails

Libraries:
<br />⮩ tkinter
<br />⮩ os
<br />⮩ csv
<br />⮩ tkcalendar