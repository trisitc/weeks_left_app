# Weeks Left Calculator

This desktop application, written in Python, allows you to calculate the number of weeks left until a specific date. It also displays a countdown timer in days, hours, and minutes.

## Features

- Enter a date in the format `YYYY-MM-DD` to calculate the number of weeks left until that date.
- If no date is entered, the application reads the date from a file named `dateparm` in the same folder. If the file does not exist or contains an invalid date, the default date of `YYYY-MM-DD` is used.
- The calculated number of weeks left is displayed in a large font below the calculate button.
- A countdown timer is shown below the result label, indicating the remaining time in days, hours, and minutes until the specified date.
- Every hour, a system sound is played to notify the user.

## Prerequisites

- Python 3.x
- `tkinter` library for the GUI interface
- `winsound` library for playing the system sound (Windows only)

## Usage

1. Run the Python script (`week_calc.py`) to launch the application.
2. Enter a date in the format `YYYY-MM-DD` into the input field.
3. Click the "Calculate" button to calculate the weeks left and display the result.
4. The result label will show the number of weeks left until the specified date.
5. The countdown label will display the remaining time in days, hours, and minutes.
6. Each hour, a system sound will be played to indicate the passage of time.

## Customization

- You can modify the default date (`2023-10-21`) by editing the code and changing the `default_date` variable in the `get_date_from_file` function.
- To change the sound played each hour, you can replace the `"SystemExclamation"` parameter in the `winsound.PlaySound` function call with the desired system sound alias.

## File Structure

- `week_calc.py`: Python script containing the main code for the desktop application.
- `dateparm` (optional): Text file containing a date in the format `YYYY-MM-DD`. If present, the application reads the date from this file.
- `README.md`: Markdown file explaining the code and usage instructions.

## License

This project is licensed under the [MIT License](LICENSE).
