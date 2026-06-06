from task_manager.validation import validate_task_title, validate_task_description, validate_due_date, validate_task_number
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def display_menu():
    print("=== Task Management System ===")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            valid_title, title_msg = validate_task_title(title)
            if not valid_title:
                print(title_msg)
                continue
            
            description = input("Enter task description: ")
            valid_desc, desc_msg = validate_task_description(description)
            if not valid_desc:
                print(desc_msg)
                continue
            
            due_date = input("Enter due date (YYYY-MM-DD): ")
            valid_date, date_msg = validate_due_date(due_date)
            if not valid_date:
                print(date_msg)
                continue
            
            add_task(tasks, title, description, due_date)
            print("Task added successfully!")
            
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue
            
            for i, task in enumerate(tasks, 1):
                status = "Complete" if task['completed'] else "Pending"
                print(f"{i}. {task['title']} - {status}")
            
            task_num = input("Enter task number to complete: ")
            valid_num, num_msg = validate_task_number(task_num, len(tasks))
            if not valid_num:
                print(num_msg)
                continue
            
            mark_task_as_complete(tasks, int(task_num) - 1)
            print("Task marked as complete!")
            
        elif choice == "3":
            view_pending_tasks(tasks)
            
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}% complete")
            
        elif choice == "5":
            print("Exiting Task Management System.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main() 