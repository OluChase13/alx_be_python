#!/bin/bash
task = input("Enter your task for today: ")
priority = input("What is the priority level of this task? (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()
match priority:
    case "high":
        reminder = "Reminder: '" + task + "' is a high priority task."
    case "medium":
        reminder = "Reminder: '" + task + "' is a medium priority task."
    case "low":
        reminder = "Reminder: '" + task + "' is a low priority task."
    case _:
        reminder = "Reminder: '" + task + "' has an unknown priority."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
    print(reminder)
elif time_bound == "no":
    reminder += "Consider completing it when you have free time"
    print(reminder)