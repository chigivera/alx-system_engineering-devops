# Load Balancer Configuration Project

This project focuses on implementing redundancy in our web infrastructure by configuring multiple web servers behind a load balancer. The setup includes configuring two web servers (web-01 and web-02) and a load balancer (lb-01) using HAProxy.

## Project Overview

### 0. Custom HTTP Response Header
**File:** `0-custom_http_response_header`
- Configures Nginx on web-01 and web-02 with custom HTTP header
- Header name: X-Served-By
- Header value: Hostname of the server
- Automated setup for new Ubuntu machines
- Ignores SC2154 for shellcheck

Example usage:
```bash
curl -sI SERVER_IP | grep X-Served-By
X-Served-By: web-01
```

### 1. Load Balancer Installation
**File:** `1-install_load_balancer`
- Installs and configures HAProxy on lb-01
- Features:
  - Round-robin load balancing algorithm
  - Traffic distribution between web-01 and web-02
  - Managed via init script
- Configures servers with correct hostnames

Example response:
```bash
curl -Is LOAD_BALANCER_IP
HTTP/1.1 200 OK
X-Served-By: web-01

curl -Is LOAD_BALANCER_IP
HTTP/1.1 200 OK
X-Served-By: web-02
```

### 2. Puppet Custom Header
**File:** `2-puppet_custom_http_response_header.pp`
- Puppet manifest for automated header configuration
- Sets up X-Served-By header with server hostname
- Configures new Ubuntu machines automatically

## Requirements

### General
- Ubuntu 16.04 LTS
- Allowed editors: vi, vim, emacs
- All files end with newline
- Bash scripts must be executable
- Scripts must pass Shellcheck (v0.3.7)
- First line: `#!/usr/bin/env bash`
- Second line: Comment explaining script purpose

### Server Configuration
Three servers are used in this setup:
- web-01: Primary web server
- web-02: Secondary web server (redundancy)
- lb-01: Load balancer

## Testing

1. Test Custom Header:
```bash
curl -sI web_server_IP | grep X-Served-By
```

2. Verify Load Balancing:
```bash
# Multiple requests should show alternating servers
curl -Is load_balancer_IP
```

3. Apply Puppet Manifest:
```bash
puppet apply 2-puppet_custom_http_response_header.pp
```