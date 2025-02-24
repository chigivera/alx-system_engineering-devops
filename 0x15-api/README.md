# API Data Gathering and Export

This project involves interacting with a REST API to gather data about employees' TODO lists and exporting the data in various formats (CSV and JSON). The scripts are written in Python and follow specific requirements.

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5)
- All files should end with a newline
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use `get` to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

---

## Tasks

### 0. Gather Data from an API
- **Script Name**: `0-gather_data_from_an_API.py`
- **Description**: Fetches and displays an employee's TODO list progress from a REST API.
- **Usage**:
  ```bash
  ./0-gather_data_from_an_API.py <employee_id>