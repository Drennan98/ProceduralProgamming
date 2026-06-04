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

def calculate_gross_pay(hours_worked, hourly_rate):
    """
    Calculate gross pay based on hours worked and hourly rate.
    """
    if hours_worked > STANDARD_HOURS:
        overtime_hours = hours_worked - STANDARD_HOURS
        regular_pay = STANDARD_HOURS * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * hourly_rate
    return gross_pay