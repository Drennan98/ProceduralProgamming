# Constants for payroll calculations. Capital letters means constant variables.

TAX_RATE = 0.20
PENSION = 0.05
STANDARD_HOURS = 40
OVERTIME_RATE = 1.5

def get_employee_details():
    """
    Collect and validate employee details.
    """
    employee_id = input("Enter employee ID: ")
    employee_name = input("Enter employee name: ")

    while True:
        try:
            hours_worked = float(input("Enter hours worked: "))
            if hours_worked < 0:
                print("Hours worked cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for hours worked.")

    while True:
        try:
            hourly_rate = float(input("Enter hourly rate: "))
            if hourly_rate < 0:
                print("Hourly rate cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for hourly rate.")

    return employee_id, employee_name, hours_worked, hourly_rate

get_employee_details()