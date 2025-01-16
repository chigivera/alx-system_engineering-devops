# Configuration Management

This project contains Puppet manifests for basic system configuration management tasks. The manifests are designed to run on Ubuntu 20.04 LTS with Puppet 5.5.

## Requirements

* Ubuntu 20.04 LTS
* Puppet 5.5
* puppet-lint 2.1.1

## Installation

Install required packages:
```bash
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
gem install puppet-lint
```

## Tasks

### 0. Create a file
`0-create_a_file.pp`: Creates a file in /tmp with specific permissions and content.
* Path: `/tmp/school`
* Permission: 0744
* Owner: www-data
* Group: www-data
* Content: "I love Puppet"

### 1. Install a package
`1-install_a_package.pp`: Installs Flask version 2.1.0 using pip3.

### 2. Execute a command
`2-execute_a_command.pp`: Creates a manifest that kills a process named killmenow using pkill.
