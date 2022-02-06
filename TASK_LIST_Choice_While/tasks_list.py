#tasks_list.py

# We define the initial auxiliary number for automating the menu selection


user_choice = -1

# We create a list of tasks
tasks = []

# We define functions that will be used below in the program 

# Load existing list
def load_existing_list():
    file = open("My_Tasks.txt")
    for line in file.readlines():
        tasks.append(line.strip())
    file.close()



# The "Show tasks" function is used to display the list of tasks
def show_tasks():
    task_index = 0
    for task in tasks:
        print(" [" + str(task_index) + "] " + task)
        task_index += 1

#The "Add tasks" function is used to add a new task to the task list. 
def add_task():
    task = input("Please type your new task: ")
    tasks.append(task)
    len_of_tasks = len(tasks) - 1
    print(f"Your new task \"{task}\" has been added to tasks list on position: [{len_of_tasks}]. ")

#The "Delete task" function prompts the user for the task number, then deletes it 
def delete_task():
    task_index = int(input("Enter the task number to be deleted from the list: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print(f"There is no task with this number: {task_index} in the task list, please press 1 to show current tasks list ")
        return
    tasks.pop(task_index)
    print(f"The indicated task number: [{task_index}] has been removed from the task list  ")


#The "Save tasks to external file" function - saves lists of tasks to .txt file.

def save_tasks_to_external_file():
    file = open("My_Tasks.txt", "w")
    task_index = 0
    for task in tasks:
        file.write(" [" + str(task_index) + "] " + task + "\n")
        task_index += 1
    file.close()

# Call funtion: load_existing_list():
try:
    load_existing_list()
except:
    pass


# The main loop of the program execution

while user_choice != 5:

    if user_choice == 1:
        print("")
        print("Your current tasks list is: ")
        show_tasks()
        
    if user_choice == 2:
        add_task()
        print("")
 
    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_external_file()



    print("")
    print("Welcome, please use unmbers from 1 to 5 only. Choose your option: ")
    print("1. Show task list ")
    print("2. Add new task to list ")
    print("3. Delete task ")
    print("4. Save changes in external file ")
    print("5. End and quit ")

    user_choice = int(input("Please choose you option, type it here and press Enter: "))