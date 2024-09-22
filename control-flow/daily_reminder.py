#!/bin/bash
task = input("Enter your task for today: ")
priority = input("What is the priority level of this task? (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()
match priority:
    case "high":
        reminder = "Reminder: '" + task + "' is of high priority."
    case "medium":
        reminder = "Reminder: '" + task + "' is of medium priority."
    case "low":
        reminder = "Reminder: '" + task + "' is of low priority."
    case _:
        reminder = "Reminder: '" + task + "' has an unknown priority."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
print(reminder)
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case high:
        print()
        