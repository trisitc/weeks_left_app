from datetime import datetime, timedelta
import os
import tkinter as tk
from tkinter import messagebox
import winsound

def get_date_from_file():
    default_date = '2023-10-21'  # Default date if 'dateparm' file doesn't exist
    if os.path.isfile('dateparm'):
        with open('dateparm', 'r') as file:
            date_str = file.read()
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            pass
    return default_date

def calculate_weeks_left():
    entered_date = date_entry.get()
    if not entered_date:
        entered_date = get_date_from_file()
    try:
        entered_date = datetime.strptime(entered_date, '%Y-%m-%d')
        current_date = datetime.now()
        weeks_left = (entered_date - current_date).days // 7
        result_label.config(text=f"There are {weeks_left} weeks left until {entered_date.date()}.", font=("Arial", 20), fg="white")

        # Calculate countdown timer
        remaining_time = entered_date - current_date
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        countdown_label.config(text=f"Countdown: {days} days, {hours:02d} hours, {minutes:02d} minutes", font=("Arial", 16), fg="white")

        # Check if an hour has passed and play a ding sound
        if hours < previous_hours:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        previous_hours = hours

    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Create the main window
window = tk.Tk()
window.title("Weeks Left Calculator")
window.geometry("400x400")
window.configure(bg="black")

# Create the label
label = tk.Label(window, text="Enter a date (YYYY-MM-DD):", font=("Arial", 20), fg="white", bg="black")
label.pack(pady=10)

# Create the entry field
date_entry = tk.Entry(window, font=("Arial", 20), fg="white", bg="black")
date_entry.pack(pady=10)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 20), bg="#4caf50", fg="white", command=calculate_weeks_left)
calculate_button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 20), fg="white", bg="black")
result_label.pack(pady=10)

# Create the countdown label
countdown_label = tk.Label(window, text="", font=("Arial", 16), fg="white", bg="black")
countdown_label.pack(pady=10)

# Initialize previous hours
previous_hours = 0

# Run the main event loop
window.mainloop()

# from datetime import datetime, timedelta
# import os
# import tkinter as tk
# from tkinter import messagebox

# def get_date_from_file():
#     default_date = '2023-10-21'  # Default date if 'dateparm' file doesn't exist
#     if os.path.isfile('dateparm'):
#         with open('dateparm', 'r') as file:
#             date_str = file.read()
#         try:
#             datetime.strptime(date_str, '%Y-%m-%d')
#             return date_str
#         except ValueError:
#             pass
#     return default_date

# def calculate_weeks_left():
#     entered_date = date_entry.get()
#     if not entered_date:
#         entered_date = get_date_from_file()
#     try:
#         entered_date = datetime.strptime(entered_date, '%Y-%m-%d')
#         current_date = datetime.now()
#         weeks_left = (entered_date - current_date).days // 7
#         result_label.config(text=f"There are {weeks_left} weeks left until {entered_date.date()}.", font=("Arial", 20), fg="white")

#         # Calculate countdown timer
#         remaining_time = entered_date - current_date
#         days = remaining_time.days
#         hours, remainder = divmod(remaining_time.seconds, 3600)
#         minutes, _ = divmod(remainder, 60)
#         countdown_label.config(text=f"Countdown: {days} days, {hours:02d} hours, {minutes:02d} minutes", font=("Arial", 16), fg="white")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")

# # Create the main window
# window = tk.Tk()
# window.title("Weeks Left Calculator")
# window.geometry("500x400")
# window.configure(bg="black")

# # Create the label
# label = tk.Label(window, text="Enter a date (YYYY-MM-DD):", font=("Arial", 20), fg="white", bg="black")
# label.pack(pady=10)

# # Create the entry field
# date_entry = tk.Entry(window, font=("Arial", 20), fg="white", bg="black")
# date_entry.pack(pady=10)

# # Create the calculate button
# calculate_button = tk.Button(window, text="Calculate", font=("Arial", 20), bg="#4caf50", fg="white", command=calculate_weeks_left)
# calculate_button.pack(pady=10)

# # Create the result label
# result_label = tk.Label(window, text="", font=("Arial", 20), fg="white", bg="black")
# result_label.pack(pady=10)

# # Create the countdown label
# countdown_label = tk.Label(window, text="", font=("Consolas", 16), fg="white", bg="black")
# countdown_label.pack(pady=10)

# # Run the main event loop
# window.mainloop()

# from datetime import datetime, timedelta
# import tkinter as tk
# from tkinter import messagebox

# def calculate_weeks_left():
#     try:
#         entered_date = datetime.strptime(date_entry.get(), '%Y-%m-%d')
#         current_date = datetime.now()
#         weeks_left = (entered_date - current_date).days // 7
#         result_label.config(text=f"There are {weeks_left} weeks left until {entered_date.date()}.", font=("Arial", 20), fg="white")
        
#         # Calculate countdown timer
#         remaining_time = entered_date - current_date
#         days = remaining_time.days
#         hours, remainder = divmod(remaining_time.seconds, 3600)
#         minutes, _ = divmod(remainder, 60)
#         countdown_label.config(text=f"Countdown: {days} days, {hours:02d} hours, {minutes:02d} minutes", font=("Arial", 16), fg="white")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")

# # Create the main window
# window = tk.Tk()
# window.title("Weeks Left Calculator")
# window.geometry("500x400")
# window.configure(bg="black")

# # Create the label
# label = tk.Label(window, text="Enter a date (YYYY-MM-DD):", font=("Arial", 20), fg="white", bg="black")
# label.pack(pady=10)

# # Create the entry field
# date_entry = tk.Entry(window, font=("Arial", 20), fg="white", bg="black")
# date_entry.pack(pady=10)

# # Create the calculate button
# calculate_button = tk.Button(window, text="Calculate", font=("Arial", 20), bg="#4caf50", fg="white", command=calculate_weeks_left)
# calculate_button.pack(pady=10)

# # Create the result label
# result_label = tk.Label(window, text="", font=("Arial", 20), fg="white", bg="black")
# result_label.pack(pady=10)

# # Create the countdown label
# countdown_label = tk.Label(window, text="", font=("Arial", 16), fg="white", bg="black")
# countdown_label.pack(pady=10)

# # Run the main event loop
# window.mainloop()

# # from datetime import datetime
# # import tkinter as tk
# # from tkinter import messagebox

# # def calculate_weeks_left():
# #     try:
# #         entered_date = datetime.strptime(date_entry.get(), '%Y-%m-%d')
# #         current_date = datetime.now()
# #         weeks_left = (entered_date - current_date).days // 7
# #         result_label.config(text=f"{weeks_left} weeks left until {entered_date.date()}.", font=("Verdana", 20), fg="white")
# #     except ValueError:
# #         messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")

# # # Create the main window
# # window = tk.Tk()
# # window.title("Weeks Left Calculator")
# # window.geometry("500x300")
# # window.configure(bg="black")

# # # Create the label
# # label = tk.Label(window, text="Enter a date (YYYY-MM-DD):", font=("Arial", 15), fg="white", bg="black")
# # label.pack(pady=10)

# # # Create the entry field
# # date_entry = tk.Entry(window, font=("Arial", 15), fg="white", bg="black")
# # date_entry.pack(pady=10)

# # # Create the calculate button
# # calculate_button = tk.Button(window, text="Calculate", font=("Arial", 15), bg="#4caf50", fg="white", command=calculate_weeks_left)
# # calculate_button.pack(pady=10)

# # # Create the result label
# # result_label = tk.Label(window, text="", font=("Arial", 20), fg="white", bg="black")
# # result_label.pack(pady=10)

# # # Run the main event loop
# # window.mainloop()
