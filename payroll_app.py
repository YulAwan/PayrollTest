#This is a payroll project
#Here we will import packages
import pywebio
from pywebio import start_server
from pywebio.input import *
#from pywebio.input import input_group
from pywebio.output import put_text, put_html, put_markdown, put_table
from pywebio.session import info as session_info

def main():
    put_markdown('# **Payroll Calculator**')


while True:
            name = input("Enter the name ")
            if not name.isalpha():
                print('ERROR. Enter only letters')
                continue
            else:
                print("Hello, ", name)
            break

def get_correct_rate(hourly_rate):
        while True:
            try:
                hourly_rate = float(input("What is hourly rate? $"))
            except ValueError:
                print("ERROR.PLease use digits for value")
                continue
            return hourly_rate
hourly_rate = get_correct_rate("What is hourly rate? $")

def get_correct_hours(hours):
    while True:
        try:
            hours = float(input("How many working hours this week? "))
        except ValueError:
            print("ERROR.PLease use digits for value")
            continue

        if hours <= 0:
            print("Sorry, your response cannot be 0 or less.")
            continue
        elif hours > 168:
            print ("Sorry, your response cannot be more than 168")
        else:
            break
    return hours
hours = get_correct_hours("How many working hours per week?")


#Here is all math

def overtime_count(hours):
    while True:
        try:
            if hours > 40:
                overtime = hours - 40
            else:
                overtime = 0 
                print ("No overtime this week")
        finally:
            return overtime

overtime = overtime_count (hours)
regular_pay = (hours - overtime) * hourly_rate
ot_pay = overtime * hourly_rate * 1.5
gross_pay = regular_pay + ot_pay
fed_tax = gross_pay * 0.15
state_tax = gross_pay * 0.05
fica = gross_pay * 0.02
net_pay = gross_pay - fed_tax - state_tax - fica


print ("Here is the employee's payroll information:\n")
print ("Employee name -",name)
print ("Hourly rate, $ ",hourly_rate)
print ("Hours worked this week ",hours)
print ("Regular pay: $",regular_pay)
print ("Overtime pay: $",ot_pay)
print ("Gross pay: $",gross_pay)
print ("Federal tax: $",fed_tax)
print ("State tax: $",state_tax)
print ("FICA: $",fica)
print ("Net Pay: $",net_pay) 

put_markdown('# **Results**')
put_html('<br><br>')
put_html('<hr>')
put_table([
                'Your Name', 'Hourly rate, $', 'Working hours', 'Regular pay, $', 'Overtime pay', 'Gross Pay', 'Fed tax', 'State tax', 'FICA', 'Net Pay'],
                [name, hourly_rate, hours, regular_pay, ot_pay, gross_pay, fed_tax, state_tax, fica, net_pay],
            ])

if __name__=="__main__":
    start_server (main, debug = True, port = 8080)
