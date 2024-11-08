# ALX System Engineering DevOps - Processes and Signals

A collection of Bash scripts for process and signal management in Unix-like systems, built with Node.js.

## Project Structure

```
.
├── index.js                 # Main Node.js entry point
└── 0x05-processes_and_signals/
    ├── 0-what-is-my-pid
    ├── 1-list_your_processes
    ├── 2-show_your_bash_pid
    ├── 3-show_your_bash_pid_made_easy
    ├── 4-to_infinity_and_beyond
    ├── 5-dont_stop_me_now
    ├── 6-stop_me_if_you_can
    ├── 7-highlander
    ├── 8-beheaded_process
    └── 67-stop_me_if_you_can
```

## Scripts Description

- `0-what-is-my-pid`: Displays the script's own PID
- `1-list_your_processes`: Shows a list of currently running processes
- `2-show_your_bash_pid`: Displays lines containing the bash word
- `3-show_your_bash_pid_made_easy`: Shows PID and process name of bash processes
- `4-to_infinity_and_beyond`: Displays a message indefinitely
- `5-dont_stop_me_now`: Stops the 4-to_infinity_and_beyond process using kill
- `6-stop_me_if_you_can`: Stops the 4-to_infinity_and_beyond process without kill
- `7-highlander`: Displays a message indefinitely and handles SIGTERM
- `8-beheaded_process`: Kills the 7-highlander process
- `67-stop_me_if_you_can`: Stops the 7-highlander process

## Getting Started

1. Clone the repository
2. Make the scripts executable:
   ```bash
   chmod +x 0x05-processes_and_signals/*
   ```
3. Run any script:
   ```bash
   ./0x05-processes_and_signals/script-name
   ```

## Node.js Application

Run the Node.js application:

```bash
node index.js
```

## Requirements

- Node.js
- Unix-like operating system (Linux, macOS)
- Bash shell

## License

This project is open source and available under the MIT License.