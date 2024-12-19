# CLI Tool

This project is a simple command-line interface (CLI) tool for managing tasks. It allows users to add, update, and delete tasks from their to-do list.

## Features

- Add tasks
- Update existing tasks
- Delete tasks
- List all tasks

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the CLI tool, run the following command:

```
python src/main.py [command] [options]
```

### Commands

- `add`: Add a new task.
  - Example: `python src/main.py add "Buy groceries"`
  
- `update`: Update an existing task.
  - Example: `python src/main.py update 1 "Buy groceries and cook dinner"`
  
- `delete`: Delete a task.
  - Example: `python src/main.py delete 1`
  
- `list`: List all tasks.
  - Example: `python src/main.py list`

## Contributing

Feel free to submit issues or pull requests to improve the CLI tool.

## License

This project is licensed under the MIT License.