# Web Server Configuration Project

This project contains scripts for configuring and managing a web server using Nginx. Each script performs specific tasks related to server setup and configuration.

## Scripts Overview

### 0. Transfer a File to Server
**File:** `0-transfer_file`
- Transfers a file from client to server using scp
- Accepts 4 parameters:
  - Path to file
  - Server IP
  - Username
  - Path to SSH private key
- Disables strict host key checking

### 1. Install Nginx Web Server
**File:** `1-install_nginx_web_server`
- Installs and configures Nginx web server
- Configures Nginx to listen on port 80
- Sets up a default page displaying "Hello World!"
- Handles installation without using systemctl

### 2. Setup Domain Name
**File:** `2-setup_a_domain_name`
- Contains the domain name for the server
- Requires:
  - Domain registration through .TECH Domains
  - A record configuration pointing to web-01 IP
  - No subdomain inclusion

### 3. Redirection
**File:** `3-redirection`
- Configures Nginx for URL redirection
- Implements 301 (Moved Permanently) redirect
- Redirects /redirect_me to specified YouTube video
- Maintains "Hello World!" at root

### 4. Custom 404 Page
**File:** `4-not_found_page_404`
- Sets up custom 404 error page
- Displays "Ceci n'est pas une page"
- Returns proper 404 HTTP code
- Maintains previous configurations

### 5. Puppet Nginx Installation
**File:** `7-puppet_install_nginx_web_server.pp`
- Puppet manifest for automated Nginx setup
- Configures:
  - Port 80 listening
  - Default page with "Hello World!"
  - 301 redirect for /redirect_me

## Requirements

- Ubuntu 16.04 LTS
- Allowed editors: vi, vim, emacs
- All files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7)
- First line of Bash scripts: `#!/usr/bin/env bash`
- Second line: Comment explaining script purpose
- No use of systemctl for process management

## Testing

Each script can be tested individually:

1. File Transfer:
```bash
./0-transfer_file file.txt 8.8.8.8 username /path/to/key
```

2. Nginx Installation:
```bash
curl localhost
# Should display: Hello World!
```

3. Redirection:
```bash
curl -sI /redirect_me/
# Should show 301 redirect
```

4. 404 Page:
```bash
curl /nonexistent
# Should display: Ceci n'est pas une page
```

5. Puppet Configuration:
```bash
puppet apply 7-puppet_install_nginx_web_server.pp
```