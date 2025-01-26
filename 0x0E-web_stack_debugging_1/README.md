# Web Stack Debugging #1

## Overview
This project focuses on debugging web stack issues, specifically dealing with Nginx configuration on Ubuntu containers. The main goal is to identify and fix issues preventing Nginx from listening on port 80.

## Project Requirements

### General
- All files interpreted on Ubuntu 20.04 LTS
- Files must end with a new line
- All Bash script files must be executable
- Scripts must pass Shellcheck without errors
- First line of Bash scripts: `#!/usr/bin/env bash`
- Second line: Comment explaining script functionality
- `wget` command is not allowed

## Tasks

### 0. Nginx likes port 80
**File:** `0-nginx_likes_port_80`

#### Requirements:
- Debug and fix Nginx installation to listen on port 80
- Nginx must be running and listening on port 80 of all active IPv4 IPs
- Write a Bash script to automate the fix
- Script should use minimum number of commands

#### Example Usage:
```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused

root@966c5664b21f:/# ./0-nginx_likes_port_80
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
...
</html>
```

### 1. Make it sweet and short
**File:** `1-debugging_made_short`

#### Requirements:
- Based on Task #0 but with stricter constraints
- Bash script must be 5 lines or less
- Must include a new line at end of file
- Cannot use:
  - Semicolons (;)
  - AND operator (&&)
  - wget
  - Previous answer file
- Service (init) must report nginx as not running

#### Example Usage:
```bash
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
...
root@966c5664b21f:/# service nginx status
 * nginx is not running
```

## Repository Information
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0E-web_stack_debugging_1`
- Files: 
  - `0-nginx_likes_port_80`
  - `1-debugging_made_short`