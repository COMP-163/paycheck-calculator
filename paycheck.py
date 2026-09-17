# Name: Madison Jones
# Date: 9/18/26
# Course: COMP 163
# Project 1: Paycheck Calculator

# Put your name after "# Name:" above. The grader checks that it is filled in.

# Read four values from the user, in this order:
name = input('Enter Employee Name: ')
hrs_work = float(input('Enter Hours Worked: '))
hr_rate = float(input('Enter Hourly Rate: '))
tax_rate = float(input('Enter Tax Rate: '))

#
# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
# Then calculate:
gross_pay = hrs_wrk * hr_rate
tax_held = 
#   gross pay     = hours worked * hourly rate
#   tax withheld  = gross pay * (tax rate / 100)
#   net pay       = gross pay - tax withheld
#
# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
