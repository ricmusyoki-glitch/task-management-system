from datetime import datetime

from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

def add_task(task_list, title, description, due_date):
    """Add a new task to task_list after validation. Returns (bool, msg)"""
    # Validate each field
    valid_title, title_msg = validate_task_title(title)
    if not valid_title:
        return False, title_msg
    
    valid_desc, desc_msg = validate_task_description(description)
    if not valid_desc:
        return False, desc_msg
    
    valid_date, date_msg = validate_due_date(due_date)
    if not valid_date:
        return False, date_msg
    
    # If all valid, create and add task
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    task_list.append(new_task)
    return True, f"Task '{title}' added successfully."

def mark_task_as_complete(task_list, title):
    """Mark task with matching title as complete. Returns (bool, msg)"""
    for task in task_list:
        if task["title"] == title:
            if task["completed"]:
                return False, f"Task '{title}' is already completed."
            task["completed"] = True
            return True, f"Task '{title}' marked as complete."
    return False, f"Error: Task '{title}' not found."

def view_pending_tasks(task_list):
    """Return list of incomplete tasks. Handles empty list."""
    pending = [task for task in task_list if not task["completed"]]
    if len(pending) == 0:
        return "No pending tasks."
    return pending

def calculate_progress(task_list):
    """Return completion percentage as float."""
    if len(task_list) == 0:
        return 0.0
    completed_count = sum(1 for task in task_list if task["completed"])
    return (completed_count / len(task_list)) * 100