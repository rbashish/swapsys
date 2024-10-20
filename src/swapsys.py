import os
import sys

# Define the ANSI escape code for color
RED = "\033[1;31m"
GREEN = "\033[32m"

def main():
    print(r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
███████╗██╗    ██╗ █████╗ ██████╗ ███████╗██╗   ██╗███████╗
██╔════╝██║    ██║██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝
███████╗██║ █╗ ██║███████║██████╔╝███████╗ ╚████╔╝ ███████╗
╚════██║██║███╗██║██╔══██║██╔═══╝ ╚════██║  ╚██╔╝  ╚════██║
███████║╚███╔███╔╝██║  ██║██║     ███████║   ██║   ███████║
╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚══════╝   ╚═╝   ╚══════╝
                                                           
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SWAPSYS - A python package to manage swap space in a Linux system.
Copyright (c) 2024 - SWAPSYS DEV
Visit https://pypi.org/swapsys to report any issue.                                         

    """)
    while True:
        print("=============================")
        print("Choose an option to continue:")
        print("=============================")
        print("1. Add swap memory")
        print("2. Remove swap memory")
        print("3. Increase swap memory")
        print("4. Decrease swap memory")
        print("5. Exit")
        print("=============================")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_swap()
        elif choice == '2':
            remove_swap()
        elif choice == '3':
            increase_swap()
        elif choice == '4':
            decrease_swap()
        elif choice == '5':
            break
        else:
            print(f"{RED}Invalid choice!!\033[0m")

def add_swap():
    size = int(input("Enter the size of the swap to be added in GB: "))
    os.system(f"sudo fallocate -l {size}G /swapfile")
    os.system("sudo chmod 600 /swapfile")
    os.system("sudo mkswap /swapfile")
    os.system("sudo swapon /swapfile")
    with open("/etc/fstab", "a") as f:
        f.write("/swapfile swap swap defaults 0 0\n")

def remove_swap():
    confirm = input("Are you sure you want to remove the swap? (y/n): ")
    if confirm.lower() == 'y':
        os.system("sudo swapoff -v /swapfile")
        os.system("sudo rm /swapfile")
        with open("/etc/fstab", "r") as f:
            lines = f.readlines()
        with open("/etc/fstab", "w") as f:
            for line in lines:
                if "/swapfile" not in line:
                    f.write(line)

def increase_swap():
    size = int(input("Enter the size to increase the swap in GB: "))
    os.system(f"sudo swapoff -v /swapfile")
    os.system(f"sudo dd if=/dev/zero of=/swapfile bs=1G count={size} oflag=append conv=notrunc")
    os.system("sudo mkswap /swapfile")
    os.system("sudo swapon /swapfile")

def decrease_swap():
    size = int(input("Enter the size to decrease the swap in GB: "))
    os.system(f"sudo swapoff -v /swapfile")
    os.system(f"sudo truncate -s -{size}G /swapfile")
    os.system("sudo mkswap /swapfile")
    os.system("sudo swapon /swapfile")

if __name__ == "__main__":
    main()