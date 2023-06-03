import tkinter as tk
from tkcalendar import Calendar


def due_date():
    selected_date = None

    def get_selected_date():
        nonlocal selected_date
        selected_date = cal.get_date()
        root.quit()

    root = tk.Tk()
    root.title("Due Date Selector")

    cal = Calendar(root)
    cal.pack()

    button = tk.Button(root, text="Select Due Dat", command=get_selected_date)
    button.pack()

    root.mainloop()

    return selected_date
