# Ethical Hacking Toolkit

This toolkit provides several functions for ethical hacking, including port scanning, dictionary attacks, and remote file manipulation via SSH. The script is designed to be user-friendly and accessible through a simple command-line interface.

## Features

- **Port Scanning**: Scan a range of ports on a target host using sockets.
- **Dictionary Attack**: Perform a dictionary attack on a login form.
- **Remote File Manipulation via SSH**: Connect to a remote host via SSH and manipulate files.

## Requirements

- Python 3.x
- `requests`
- `paramiko`
- `colorama`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ethical-hacking-toolkit.git
   cd ethical-hacking-toolkit


## Usage:

Run the script and follow the prompts to choose a function and provide necessary inputs.
python ethical_hacking_toolkit.py
Or download the .exe

## Port Scanning
Choose the "Port Scan" option.
Enter the IP address of the target host.
The script will scan ports from 1 to 1024 and display the open ports.

## Dictionary Attack
Choose the "Dictionary Attack" option.
Enter the target URL.
Enter the username for the login form.
Provide the path to the password dictionary file.
The script will attempt to login using each password in the dictionary.

## Remote File Manipulation via SSH
Choose the "Manipulate Remote Files via SSH" option.
Enter the SSH hostname.
Enter the SSH port.
Enter the SSH username and password.
The script will connect to the remote host and list files in the home directory.

