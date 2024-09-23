#!/bin/bash
task = input("Enter your task for today: ").strip().capitalize()
priority = input("What is the priority level of this task? (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").strip().lower()
yes_time = "that requires immediate attention today!"
no_time = "consider completing when you have time"

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task {yes_time}")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a {priority} priority task {no_time}")
    
    case "medium":
        if time_bound == "yes":
            print(f"Attention: '{task}' is a {priority} priority task {yes_time}")
        elif time_bound == "no":
            print(f"Attention: '{task}' is a {priority} priority task {yes_time}")

    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a {priority} priority task {yes_time}")
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task {yes_time}")
            