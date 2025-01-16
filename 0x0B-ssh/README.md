# SSH Configuration Project

This project contains scripts and configuration files for setting up and managing SSH connections securely.

## Files Description

### 0-use_a_private_key
- Bash script that connects to a server using a private key
- Uses the private key `~/.ssh/school`
- Connects with user `ubuntu`
- Only uses single-character ssh flags

### 1-create_ssh_key_pair
- Bash script that creates an RSA key pair
- Creates private key named `school`
- Uses 4096 bits for key generation
- Protects the key with passphrase `betty`

### 2-ssh_config
- SSH client configuration file
- Configures the client to:
  - Use private key `~/.ssh/school`
  - Disable password authentication
  - Set various SSH options for security

### 100-puppet_ssh_config.pp
- Puppet manifest for SSH client configuration
- Automatically configures:
  - Password authentication disabled
  - Default identity file set to `~/.ssh/school`

## Requirements
- Ubuntu 20.04 LTS
- All scripts must be executable
- All files should end with a new line
- All Bash scripts must start with `#!/usr/bin/env bash`
- Puppet manifests must pass puppet-lint without any errors

## Usage

### Using the Private Key
```bash
./0-use_a_private_key
```

### Creating SSH Key Pair
```bash
./1-create_ssh_key_pair
```

### Applying Puppet Configuration
```bash
sudo puppet apply 100-puppet_ssh_config.pp
```
