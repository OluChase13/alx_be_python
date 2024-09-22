#!/bin/bash
Task = input("Enter your task for today: ")
Priority = input("What is the priority level of this task? (high, medium, low): ").lower()
Time_bound = input("Is the task time-sensitive? (yes or no): ").lower()
match Priority:
    case "high":
        reminder = "Reminder: '" + Task + "' is a high priority task."
    case "medium":
        reminder = "Reminder: '" + Task + "' is a medium priority task."
    case "low":
        reminder = "Reminder: '" + Task + "' is a low priority task."
    case _:
        reminder = "Reminder: '" + Task + "' has an unknown priority."
if Time_bound == "yes":
    reminder += " It requires immediate attention today!"
    print(reminder)