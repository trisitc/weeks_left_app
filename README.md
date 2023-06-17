# Weeks Left Calculator Application

The Weeks Left Calculator is a simple application that calculates the number of weeks left between the current date and a user-provided date. It also displays a countdown timer showing the remaining days, hours, and minutes until the target date.

## Features

- Users can enter a target date in the format YYYY-MM-DD.
- If no date is entered, the application will use a default date retrieved from a file called 'dateparm'.
- The application calculates the number of weeks left until the target date.
- It displays the result in a label, showing the number of weeks left until the target date.
- The application also shows a countdown timer, indicating the remaining days, hours, and minutes until the target date.
- If an hour has passed since the last check, the application plays a sound to notify the user.

## How to Use

1. Launch the application.
2. Enter the target date in the 'Enter a date (YYYY-MM-DD)' field. If left blank, the default date will be used.
3. Click the 'Calculate' button.
4. The application will display the number of weeks left until the target date in a label.
5. It will also show a countdown timer indicating the remaining days, hours, and minutes until the target date.
6. If an hour has passed, the application will play a sound to notify the user.
7. To change the target date, simply update the 'Enter a date (YYYY-MM-DD)' field and click 'Calculate' again.
8. The application will recalculate and display the updated results.

Note: The default date can be set by modifying the 'dateparm' file. If the file doesn't exist or contains an invalid date format, a default date of '2023-10-21' will be used.

## Code Explanation

The code is written in Python and uses the Tkinter library for creating the graphical user interface (GUI). Here's an overview of the code:

- The `get_date_from_file()` function reads the target date from the 'dateparm' file. If the file doesn't exist or contains an invalid date format, a default date is returned.
- The `calculate_weeks_left()` function is called when the user clicks the 'Calculate' button. It retrieves the entered date from the input field and calculates the number of weeks left until the target date.
- The function also updates the result label with the calculated number of weeks left and displays a countdown timer.
- It checks if an hour has passed since the last check and plays a sound if it has.
- The main window is created using Tkinter, and the necessary labels, entry field, and button are added to the window.
- The `previous_hours` variable is used to keep track of the previous hour to check if an hour has passed.

## License

The Weeks Left Calculator application is licensed under the MIT License.

MIT License
-----------

[MIT License](https://opensource.org/licenses/MIT)

