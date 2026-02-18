from tkinter import *

from tkinter import ttk

import calendar


def showCal():
    new_window = Tk()

    new_window.config(background="white")

    new_window.title("Calendar")

    #increased horizontal size of the window to fit the event list
    new_window.geometry("950x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    #Create frames on the sides of the windows so that both the calendar and event list can sit horizontally side by side
    left_frame = Frame(new_window)
    left_frame.grid(row=0, column=0, padx=10, pady=10,)
    right_frame = Frame(new_window)
    right_frame.grid(row=0, column=1, padx=10, pady=10,)

    cal_year = Label(left_frame, text=cal_content, font="Consolas 10 bold")
    cal_year.pack()
    
    #global variables to use with add/remove event functions
    global event_name_field, event_date_field, event_table

    event_label = Label(right_frame, text="Add Event", font=("Consolas", 10))
    event_label.pack()
    
    #create the widget requesting / accepting a name for the event the user wants to add
    event_name_label = Label(right_frame, text="Event Name:")
    event_name_label.pack(anchor="w")
    event_name_field = Entry(right_frame)
    event_name_field.pack(fill="x")

    #create the widget requestion / accepting the date for the event the user wants to add
    event_date_label = Label(right_frame, text="Event Date (YYYY-MM-DD):")
    event_date_label.pack(anchor="w")
    event_date_field = Entry(right_frame)
    event_date_field.pack(fill="x")

    #create the button widgets which call the functions to add and delete the event
    add_button = Button(right_frame, text="Add Event", command=addEvent)
    add_button.pack(pady=5)
    delete_button = Button(right_frame, text="Delete Selected Event", command=deleteEvent)
    delete_button.pack(pady=5)

    #create a treeview widget to display and allow selection of the events currently in the list
    columns = ("Event Name", "Event Date")
    event_table = ttk.Treeview(right_frame, columns=(1,2), show="headings", height=15)
    event_table.heading(1, text="Event Name")
    event_table.heading(2, text="Event Date")
    event_table.column(1, width=200)
    event_table.column(2, width=200)
    event_table.pack(pady=10, fill="both")

    new_window.mainloop()

    
#function to add event from the input field into the table, then clear the input field
def addEvent():
    name = event_name_field.get()
    date = event_date_field.get()

    if name and date:
        event_table.insert("", END, values=(name, date))
        event_name_field.delete(0, END)
        event_date_field.delete(0, END)

#function to delete the selected item from the table, then to create a popup confirming that an item has been deleted
def deleteEvent():
    selected_item = event_table.selection()
    if selected_item:
        for item in selected_item:
            event_table.delete(item)

        popup = Toplevel()
        popup.title("Deletion Confirmed")
        popup.geometry("200x75")
        Label(popup, text="Deletion confirmed", font=("Consolas", 10)).pack()
        Button(popup, text="OK", command=popup.destroy).pack(pady=10)


if __name__ == "__main__":
    root = Tk()

    root.config(background="white")

    root.title("HOME")

    root.geometry("500x400")

    cal = Label(
        root,
        text="Welcome to the calendar Application",
        bg="Green",
        font=("times", 20, "bold"),
    )

    year = Label(root, text="Please enter a year", bg="Green")

    year_field = Entry(root)

    Show = Button(
        root, text="Show Calendar", fg="Black", bg="Light Green", command=showCal
    )

    Exit = Button(root, text="Exit", fg="Black", bg="Light Green", command=exit)

    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    root.mainloop()
