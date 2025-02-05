# ALX System Engineering DevOps - HTTPS & SSL

## 0. World Wide Web
### Configure Your Domain Zone and Bash Script for Subdomains

### Requirements:
- Configure DNS records:
  - `www` → `lb-01` IP
  - `lb-01` → `lb-01` IP
  - `web-01` → `web-01` IP
  - `web-02` → `web-02` IP
- Create a Bash script:
  - Accepts `domain` (mandatory) and `subdomain` (optional)
  - Uses `dig`, `awk`, and at least one Bash function
  - Displays DNS record type and destination IP
  
### Example Usage:
```bash
./0-world_wide_web example.com
./0-world_wide_web example.com web-02
```

## 1. HAProxy SSL Termination
### Setting Up SSL on HAProxy

### Requirements:
- Install HAProxy 1.5+
- Obtain SSL certificate via `certbot`
- Configure HAProxy to:
  - Listen on TCP 443
  - Accept SSL traffic
  - Serve HTTPS content from the backend
- The root domain (`/`) should return a page containing `ALX`

### Example Check:
```bash
curl -sI https://www.example.com
curl https://www.example.com
```

## 2. Enforce HTTPS Traffic
### Redirect HTTP to HTTPS

### Requirements:
- Configure HAProxy to:
  - Redirect HTTP (port 80) to HTTPS (port 443) with a `301` response
  - Ensure all traffic is securely encrypted

### Example Check:
```bash
curl -sIL http://www.example.com
```

## File Structure:
- `0-world_wide_web` → Bash script for subdomain resolution
- `1-haproxy_ssl_termination` → HAProxy config for SSL termination
- `100-redirect_http_to_https` → HAProxy config for HTTP to HTTPS redirection

