from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

def display_menu():
    print("\n=== Task Management System ===")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")

def main():
    tasks = []  # Main task list
    
    while True:  # This is the loop that makes 'continue' work
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Validate title immediately
            title = input("Enter task title: ")
            valid_title, title_msg = validate_task_title(title)
            if not valid_title:
                print(title_msg)
                continue  # Skips to next loop iteration
            
            # Only ask for description if title is good
            description = input("Enter task description: ")
            valid_desc, desc_msg = validate_task_description(description)
            if not valid_desc:
                print(desc_msg)
                continue
            
            # Only ask for date if description is good  
            due_date = input("Enter due date (YYYY-MM-DD): ")
            valid_date, date_msg = validate_due_date(due_date)
            if not valid_date:
                print(date_msg)
                continue
            
            # If we got here, all 3 are valid
            success, message = add_task(tasks, title, description, due_date)
            print(message)
            
        elif choice == "2":
            title = input("Enter task title to complete: ")
            success, message = mark_task_as_complete(tasks, title)
            print(message)
            
        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if isinstance(pending, str):
                print(pending)
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"- {task['title']}: {task['description']} | Due: {task['due_date']}")
                    
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.1f}% complete")
            
        elif choice == "5":
            print("Exiting Task Management System.")
            break
            
        else:
            print("Error: Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()