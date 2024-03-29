def main_menu():
  while True:
    print('\n=== Todo List ===')
    print('1. Create task')
    print('2. List all tasks')
    print('3. Get task by ID')
    print('4. Update task by ID')
    print('5. Delete task by ID')
    print('6. Exit')

    choice = input('Enter a corrisponding number, to make a choice: ')

    if choice == '1':
      create_task()
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      get_task_byId()
    elif choice == '4':
      update_task_by_id()
    elif choice == '5':
      delete_task_by_id()
    elif choice == '6':
      break
    else:
      print('Invalid choice. Please try again')

def create_task():
  task = input('Please type in your task: ')
  formattedTask = f'{len(tasks) + 1}. {task}'
  tasks.append(formattedTask)

def list_tasks():
  print(tasks)

def get_task_byId():
    task_id = input('Please input the task ID: ')
    filtered_tasks = [task for task in tasks if task.startswith(task_id + '.')]
    if not filtered_tasks:
        print('No task with that ID found')
    print(filtered_tasks)

def update_task_by_id():
  task_id = input('Please input the task ID: ')
  updatedTask = input('Update to apply: ')
  index = next((i for i, task in enumerate(tasks) if task.startswith(task_id + '.')), None)
  tasks[index] = f'{task_id}. {updatedTask}'
  print(f'task at index {index} updated.')

def delete_task_by_id():
  global tasks
  task_id = input('Please input the task ID: ')
  index = next((i for i, task in enumerate(tasks) if task.startswith(task_id + '.')), None)
  tasks.pop(index)
  tasks = [f'{i+1}. {task.split(". ", 1)[1]}' for i, task in enumerate(tasks)]
  print(f'Task with ID {task_id} deleted')

tasks = []

if __name__ == '__main__':
  main_menu()