# 0x12. Web Stack Debugging #2

## Description
This project focuses on debugging and configuring web stack issues in a containerized environment. You will be working with user permissions, process management, and ensuring that services run under the correct users.

## Requirements
- All scripts will be interpreted on **Ubuntu 20.04 LTS**.
- All files should end with a **new line**.
- A **README.md** file at the root of the project is mandatory.
- All Bash scripts must be **executable**.
- Bash scripts must pass **Shellcheck** without any error.
- Bash scripts must run without error.
- The first line of all Bash scripts should be exactly:
  ```bash
  #!/usr/bin/env bash
  ```
- The second line of all Bash scripts must be a comment explaining what the script does.

---

## Tasks

### 0. Run software as another user
**File:** `0-iamsomeoneelse`

#### Description
A script that runs the `whoami` command under a specified user.

#### Requirements
- The script accepts **one argument** (username).
- It runs the `whoami` command under the given user.
- Test the script by passing different users.

#### Example
```bash
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
```

---

### 1. Run Nginx as Nginx
**File:** `1-run_nginx_as_nginx`

#### Description
By default, **Nginx** runs as the **root** user. This script ensures that Nginx runs under the **nginx** user for security purposes.

#### Requirements
- Nginx must run under the `nginx` user.
- Nginx must listen on **port 8080** on all active IPs.
- **Do not** use `apt-get remove`.
- The script configures the container to meet these requirements.

#### Expected Output
```bash
root@container:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
```

#### Verify
Run the following command to check if Nginx is listening on port **8080**:
```bash
nc -z 0 8080 ; echo $?
0
```

---

### 2. 7 Lines or Less
**File:** `100-fix_in_7_lines_or_less`

#### Description
This task requires optimizing the solution for Task #1 to **7 lines or less**.

#### Requirements
- The script **must be 7 lines or less**.
- The script **must end with a new line**.
- Follow all **Bash script requirements**.
- **Do not** use `;`, `&&`, `wget`, or execute the previous script.

---

## Usage
Ensure scripts are executable before running:
```bash
chmod +x script_name.sh
./script_name.sh
```

---

## Author
Ayman Benchamkha

