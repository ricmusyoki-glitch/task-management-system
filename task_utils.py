def add_task(tasks, title, description, due_date):
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)

def mark_task_as_complete(tasks, task_index):
    tasks[task_index]['completed'] = True

def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task['completed']]
    if not pending:
        print("No pending tasks.")
        return
    
    for task in pending: 
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print("-" * 20)

def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for task in tasks if task['completed'])
    return (completed / len(tasks)) * 100