# import subprocess
# import tkinter as tk
# from tkinter import simpledialog
# from subprocess import Popen, PIPE

# def get_interfaces():
#     interfaces = []
#     try:
#         output = subprocess.check_output(["ifconfig"])
#         output = output.decode("utf-8")
#         lines = output.split("\n")
#         for line in lines:
#             if line.startswith("en") or line.startswith("eth"):
#                 interface = line.split(":")[0]
#                 interfaces.append(interface)
#     except subprocess.CalledProcessError:
#         print("Failed to retrieve network interfaces.")
#     return interfaces

# def get_mac(interface):
#     try:
#         output = subprocess.check_output(["ifconfig", interface])
#         output = output.decode("utf-8")
#         lines = output.split("\n")
#         for line in lines:
#             if "ether" in line:
#                 mac_address = line.split("ether")[1].strip()
#                 return mac_address
#     except subprocess.CalledProcessError:
#         print(f"Failed to retrieve MAC address for {interface}.")
#     return None

# def run_command_with_sudo(command):
#     # Acquire the lock
#         # Ask for the sudo password using a text input dialog
#     password = simpledialog.askstring("Sudo Password", "Enter your sudo password:", show='*')
#         # Construct the sudo command with the provided password
#     sudo_command = f"echo '{password}' | sudo -S {command}"
  
#     # Execute the sudo command
#     process =Popen(sudo_command, shell=True, stdout=PIPE, stderr=PIPE)
#     for line in process.stdout:
#                         output = line.decode("utf-8").strip()  # Decode and strip each line of output from the subprocess
#                         print(output)  # Print the output
#     return process.stdout





# def set_mac():
#     try:
#         run_command_with_sudo(['sh randoMac.sh'])

       
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to set MAC address: {e}")


# def create_gui():
#     window = tk.Tk()
#     window.title("MAC Address Changer")

#     adapter_label = tk.Label(window, text="Adapter:")
#     adapter_label.pack()
#     interfaces = get_interfaces()
#     if not interfaces:
#         print("No network interfaces found.")
#         return

#     adapter_var = tk.StringVar(window)
#     # adapter_var.set(interfaces['en0'])  # Set the default adapter
#     adapter_var.set('en0')
#     adapter_dropdown = tk.OptionMenu(window, adapter_var, *interfaces)
#     adapter_dropdown.pack()

#     set_mac_button = tk.Button(window, text="Random MAC Address", command=set_mac)
#     set_mac_button.pack()

#     interfaces = get_interfaces()
#     if not interfaces:
#         print("No network interfaces found.")
#         return

#     for interface in interfaces:
#         mac_address = get_mac(interface)
#         if interface == 'en0':
#             if mac_address:
#                 label = tk.Label(window, text=f"{interface}:")
#                 label.pack()
#                 value = tk.Label(window, text=mac_address)
#                 value.pack()

#     window.mainloop()

# create_gui()

import subprocess
import tkinter as tk
from tkinter import simpledialog
from subprocess import Popen, PIPE

# Get a list of network interfaces
def get_interfaces():
    interfaces = []
    try:
        output = subprocess.check_output(["ifconfig"])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if line.startswith("en") or line.startswith("eth"):
                interface = line.split(":")[0]
                interfaces.append(interface)
    except subprocess.CalledProcessError:
        print("Failed to retrieve network interfaces.")
    return interfaces

# Get the MAC address for a given interface
def get_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if "ether" in line:
                mac_address = line.split("ether")[1].strip()
                return mac_address
    except subprocess.CalledProcessError:
        print(f"Failed to retrieve MAC address for {interface}.")
    return None

# Run a command with sudo privileges
def run_command_with_sudo(command):
    # Acquire the lock
    # Ask for the sudo password using a text input dialog
    password = simpledialog.askstring("Sudo Password", "Enter your sudo password:", show='*')
    # Construct the sudo command with the provided password
    sudo_command = f"echo '{password}' | sudo -S {command}"
  
    # Execute the sudo command
    process = Popen(sudo_command, shell=True, stdout=PIPE, stderr=PIPE)
    for line in process.stdout:
        output = line.decode("utf-8").strip()  # Decode and strip each line of output from the subprocess
        print(output)  # Print the output
    return process.stdout

# Set the MAC address using a random MAC address script
def set_mac():
    try:
        run_command_with_sudo(['sh randoMac.sh'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to set MAC address: {e}")

# Create the GUI for the MAC Address Changer
def create_gui():
    window = tk.Tk()
    window.title("MAC Address Changer")

    adapter_label = tk.Label(window, text="Adapter:")
    adapter_label.pack()
    interfaces = get_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        return

    adapter_var = tk.StringVar(window)
    # adapter_var.set(interfaces['en0'])  # Set the default adapter
    adapter_var.set('en0')
    adapter_dropdown = tk.OptionMenu(window, adapter_var, *interfaces)
    adapter_dropdown.pack()

    set_mac_button = tk.Button(window, text="Random MAC Address", command=set_mac)
    set_mac_button.pack()

    interfaces = get_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        return

    for interface in interfaces:
        mac_address = get_mac(interface)
        if interface == 'en0':
            if mac_address:
                label = tk.Label(window, text=f"{interface}:")
                label.pack()
                value = tk.Label(window, text=mac_address)
                value.pack()

    window.mainloop()

# Run the GUI
create_gui()