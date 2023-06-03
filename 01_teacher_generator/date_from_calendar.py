import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def due_date():
    root = tk.Tk()
    root.title("Due Date Selector")

    #function which is invoked after pressing "Select Date" button
    def get_selected_date():
        selected_date = cal.get_date()
        print("Due Date:", selected_date)
        #closing the window
        root.destroy()

    cal = Calendar(root)
    #calendar widget in main window
    cal.pack()

    #button will invoke the get_selected_date() function after click
    button = ttk.Button(root, text="Select Due Date", command=get_selected_date)
    #button in main window
    button.pack()

    #start main event loop
    root.mainloop()
