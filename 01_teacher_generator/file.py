import tkinter as tk
from tkinter import filedialog
import os
import csv


def is_csv_file(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if not file_path:
        raise FileNotFoundError("No file selectedd")
    if file_extension.lower() != '.csv':
        raise TypeError("Wrong file type")


def check_if_file_correct():
    while True:
        try:
            file_path = get_path()
            is_csv_file(file_path)
            with open(file_path, 'r') as csvfile:
                csv.reader(csvfile, delimiter=';')
                break
        except (FileNotFoundError, TypeError) as e:
            print(f"\033[3m{e}\033[0m")

    return file_path


def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path
