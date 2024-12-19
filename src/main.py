import argparse
from utils import task_manager

def main():
    parser = argparse.ArgumentParser(description='A simple CLI tool for managing tasks.')
    parser.add_argument('action', choices=['add', 'update', 'delete', 'list'], help='Action to perform on tasks')
    parser.add_argument('--task', type=str, help='Task description')
    parser.add_argument('--id', type=int, help='Task ID for updating or deleting')

    args = parser.parse_args()

    if args.action == 'add':
        if args.task:
            task_manager.add_task(args.task)
            print(f'Task added: {args.task}')
        else:
            print('Task description is required for adding a task.')

    elif args.action == 'update':
        if args.id is not None and args.task:
            task_manager.update_task(args.id, args.task)
            print(f'Task updated: {args.task}')
        else:
            print('Task ID and new description are required for updating a task.')

    elif args.action == 'delete':
        if args.id is not None:
            task_manager.delete_task(args.id)
            print(f'Task with ID {args.id} deleted.')
        else:
            print('Task ID is required for deleting a task.')

    elif args.action == 'list':
        tasks = task_manager.list_tasks()
        for task in tasks:
            print(f'ID: {task["id"]}, Description: {task["description"]}')

if __name__ == '__main__':
    main()