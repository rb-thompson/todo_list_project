import json
import random
from colorama import init, Fore, Style
init()  # Initialize colorama

# Save tasks to a file
def save_tasks(task_list, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(task_list, file)
    print("Tasks saved successfully.")

# Load tasks from a file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Initialize tasks
tasks = load_tasks()

# Add a task to the list
def add_task(task_list, new_task):
    task_list.append(new_task)
    print(f"Task '{new_task}' added to the list.")

# Remove a task from the list
def remove_task(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        removed_task = task_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index.")

# List all tasks
def list_tasks(task_list):
    if not task_list:
        print(f"{Fore.YELLOW}No tasks in the list.{Style.RESET_ALL}")
    else:
        for index, task in enumerate(task_list, 1):
            print(f"{Fore.CYAN}{index}.{Style.RESET_ALL} {task}")

# Randomly select a task
def random_task(task_list):
    if not task_list:
        print(f"{Fore.YELLOW}No tasks in the list.{Style.RESET_ALL}")
    else:
        selected_task = random.choice(task_list)
        print(f"{Fore.GREEN}Selected task:{Style.RESET_ALL} {selected_task}")

# Program Information
def program_info():
    print(f"{Fore.YELLOW}Welcome to the Task Manager!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}This program allows you to manage your tasks.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}You can add, list, remove, or randomly select tasks.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'exit' to save and quit.{Style.RESET_ALL}") 

# Main loop
while True:
    print(f"\n{Fore.BLUE}Available actions:{Style.RESET_ALL} add, list, remove, random, info, exit")
    action = input("What would you like to do? ")

    if action == 'add':
        new_task = input("Enter new task: ")
        add_task(tasks, new_task)
        print(f"{Fore.GREEN}Task added successfully!{Style.RESET_ALL}")
    elif action == 'list':
        list_tasks(tasks)
    elif action == 'remove':
        task_index = int(input("Enter task index to remove: "))
        remove_task(tasks, task_index)
    elif action == 'random':
        random_task(tasks)
    elif action == 'info':
        program_info()
    elif action == 'exit':
        save_tasks(tasks)
        print("Goodbye!")
        break
    else:
        print(f"{Fore.RED}Invalid action. Please choose 'add', 'list', 'remove', 'random', 'info', or 'exit'.{Style.RESET_ALL}")

