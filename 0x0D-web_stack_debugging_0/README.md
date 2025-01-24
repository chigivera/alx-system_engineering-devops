# Web Stack Debugging: 0-give_me_a_page

This project is part of the **ALX System Engineering & DevOps** curriculum. The goal is to debug a web stack by ensuring that Apache runs on a Docker container and serves a page containing "Hello ALX" when queried at the root URL.

## Task Overview

The task involves:
1. Starting a Docker container.
2. Installing and configuring Apache.
3. Creating a simple HTML page.
4. Writing a Bash script to automate the process.

## Requirements
- Docker must be installed on your machine.
- The Docker container should be running Ubuntu 14.04 or a compatible version.
- The Bash script must be executable and pass **Shellcheck** without errors.

## Files
- **`0-give_me_a_page`**: Bash script to fix the issue and serve the "Hello ALX" page.
- **`README.md`**: This file provides an overview of the project.

---

## Steps to Reproduce and Fix the Issue

### 1. Start the Docker Container
Run the Docker container with port mapping:

```bash
docker run -p 8080:80 -d -it alx/265-0
