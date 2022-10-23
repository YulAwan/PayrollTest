#This is a payroll project
#Here we will import packages


#Here we will collect the data from user

name = input("Enter the name ")

while True:
    name = input("Enter the name ")
    if not name.isalpha():
        print('ERROR. Enter only letters')
        continue
    else:
        print("Hello, ", name)
    break
    
"""
def get_name(name):
    while True:
        try:
            name = input("Enter the name ")
        except:
            if not name.isalpha():
                print("ERROR.PLease use alpha characters")
                continue
            else:
                break
name = get_name("Enter the name")

"""


#name = input("Enter the name of a person: ")
#if not name.isalpha():
#    print ("ERROR. Please, enter the name using alpha")
#    
#    exit()

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
"""
def payroll_calculator(hours, hourly_rate):
    while True:
        try:
            overtime = hours - 160
            regular_pay = hours * hourly_rate
            ot_pay = overtime * hourly_rate * 1.5
            gross_pay = regular_pay + ot_pay
            fed_tax = gross_pay * 0.15
            state_tax = gross_pay * 0.05
            fica = gross_pay * 0.02
            net_pay = gross_pay - fed_tax - state_tax - fica
        finally:
            break
    return net_pay

net_pay = payroll_calculator(hours, hourly_rate)
print (net_pay)
gross_pay = payroll_calculator (hours, hourly_rate)
print (gross_pay)

"""
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
#print (overtime)

regular_pay = (hours - overtime) * hourly_rate
ot_pay = overtime * hourly_rate * 1.5
gross_pay = regular_pay + ot_pay
fed_tax = gross_pay * 0.15
state_tax = gross_pay * 0.05
fica = gross_pay * 0.02
net_pay = gross_pay - fed_tax - state_tax - fica



#Here is our output
#payroll_dict = {name: [hourly_rate, hours, regular_pay, ot_pay, gross_pay, 
#fed_tax, state_tax, fica, net_pay]}
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

