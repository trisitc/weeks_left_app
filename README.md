# Weeks Left Calculator

![Weeks Left Calculator](weekscalc.png)

The Weeks Left Calculator is a simple desktop application built with Python and Tkinter that calculates the number of weeks left between a user-specified date and the current date. It provides a countdown timer and displays the result in weeks.

## Features
- Calculates the number of weeks left until a specified date
- Automatically updates the countdown timer at regular intervals
- Plays a sound notification when an hour has passed since the last update
- Retrieves the default date from a file
- Allows the user to enter a custom date
- Validates the date format and displays an error message if it's invalid

## How to Use
1. Clone or download the repository to your local machine.
2. Install the required dependencies, such as Tkinter (if not already installed).
3. Run the `weeks_left_app.py` script.
4. The application window will open, displaying the countdown timer and result label.
5. By default, the app retrieves the date from the `dateparm` file. If the file doesn't exist or the date is invalid, it uses a default date.
6. To calculate the weeks left, enter a date in the format `YYYY-MM-DD` in the entry field.
7. Click the "Calculate" button to update the countdown timer and result label.
8. The countdown timer will automatically update every minute.
9. If an hour has passed since the last update, a sound notification will play.

## License
This project is licensed under the [MIT License](LICENSE).

---

_Enjoy tracking the weeks left with a touch of fun!_ 🎉
