from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        return False, "Title cannot be empty."
    if len(title) > 100:
        return False, "Title cannot exceed 100 characters."
    return True, ""

def validate_task_description(description):
    if len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    return True, ""

def validate_due_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."
    return True, ""

def validate_task_number(num_str, max_num):
    try:
        num = int(num_str)
    except ValueError:
        return False, "Please enter a valid number."
    
    if num < 1 or num > max_num:
        return False, f"Please enter a number between 1 and {max_num}."
    return True, ""