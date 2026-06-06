from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        return False, "Error: Title cannot be empty."
    if len(title) > 50:
        return False, "Error: Title must be 50 characters or less."
    return True, ""

def validate_task_description(description):
    if len(description) == 0:
        return False, "Error: Description cannot be empty."
    if len(description) > 200:
        return False, "Error: Description must be 200 characters or less."
    return True, ""

def validate_due_date(due_date):
    if len(due_date) == 0:
        return False, "Error: Due date cannot be empty."
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Error: Due date must be in YYYY-MM-DD format."