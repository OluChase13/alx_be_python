#!/bin/bash
monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(total_monthly_expenses)
print("Your monthly savings are $" + str(monthly_savings))
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $" + str(projected_savings))