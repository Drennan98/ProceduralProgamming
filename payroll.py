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


def calculate_tax(gross_pay):
    """
    Calculate tax based on gross pay.
    """
    return gross_pay * TAX_RATE


def calculate_pension(gross_pay):
    """
    Calculate pension contributionss based on gross pay.
    """
    return gross_pay * PENSION


def calculate_net_pay(gross_pay, tax, pension):
    """
    Calculate the net pay after deducting tax and pension from gross pay.
    """
    return gross_pay - tax - pension


def display_payslip(employee_id, employee_name,
                    hours_worked, hourly_rate,
                    gross_pay, tax,
                    pension, net_pay):
     """
     Function which will display employee payslip with all the details.
     """

     print("\n" + "=" * 40)
     print("\n--- Employee Payslip ---")
     print("=" * 40)

     print(f"Employee ID: {employee_id}")
     print(f"Employee Name: {employee_name}")
     print(f"Hours Worked: {hours_worked:.2f}")
     print(f"Hourly Rate: €{hourly_rate:.2f}")

     print("-" * 40)

     print(f"Gross Pay: €{gross_pay:.2f}")
     print(f"Tax Deduction: €{tax:.2f}")
     print(f"Pension Contribution: €{pension:.2f}")
     print(f"Net Pay: €{net_pay:.2f}")


def save_payslip(employee_id, employee_name,
                 gross_pay, tax,
                 pension, net_pay):
    """
    Writing payroll information to txt file.
    """

    with open("payslip.txt", "a") as file:
        file.write("\n")
        file.write("=" * 40 + "\n")
        file.write("GOLF SHOP PAYSLIP\n")
        file.write("=" * 40 + "\n")

        file.write(f"Employee ID: {employee_id}\n")
        file.write(f"Employee Name: {employee_name}\n")
        
        file.write(f"Gross Pay: €{gross_pay:.2f}\n")
        file.write(f"Tax Deduction: €{tax:.2f}\n")
        file.write(f"Pension Contribution: €{pension:.2f}\n")
        file.write(f"Net Pay: €{net_pay:.2f}\n")

        file.write(f"=" * 40 + "\n")


def display_summary(total_gross_pay,
                    total_net_pay,
                    number_of_employees):
    """
    Displays the total number of employees processed, total gross pay, and total net pay.
    """

    average_net_pay = total_net_pay / number_of_employees

    print("\n")
    print("=" * 40)
    print("Golf Shop Payroll Summary")
    print("=" * 40)

    print(f"Employees Processed: {number_of_employees}")
    print(f"Total Gross Pay: €{total_gross_pay:.2f}")
    print(f"Total Net Pay: €{total_net_pay:.2f}")
    print(f"Average Net Pay: €{average_net_pay:.2f}")

    print("=" * 40)

def main():

    print("Payroll Processing System")

    while True:
        try:
            number_of_employees = int(
                input("Enter the number of employees to process: "))
            
            if number_of_employees <= 0:
                print("Number of employees must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid whole number for employees.")

    total_gross_pay = 0
    total_net_pay = 0

    # Hit enter to reduce the line size to adhere to PEP8 standards. 
    for employee in range(number_of_employees):
        
        print (f"\nEmployee {employee + 1}")
        
        employee_id, employee_name, hours_worked, hourly_rate = \
            get_employee_details()
            
        gross_pay = calculate_gross_pay(
            hours_worked, 
            hourly_rate
        )

        # Function calls to calculate tax and pension contributions based on gross pay.
        tax = calculate_tax(gross_pay)
        pension = calculate_pension(gross_pay)

        net_pay = calculate_net_pay(
            gross_pay,
            tax,
            pension
        )

        display_payslip(
            employee_id,
            employee_name,
            hours_worked,
            hourly_rate,
            gross_pay,
            tax,
            pension,
            net_pay
        )

        save_payslip(
            employee_id,
            employee_name,
            gross_pay,
            tax,
            pension,
            net_pay 
        )

        total_gross_pay += gross_pay
        total_net_pay += net_pay

    display_summary(
        total_gross_pay,
        total_net_pay,
        number_of_employees
        )


if __name__ == "__main__":
    main()
