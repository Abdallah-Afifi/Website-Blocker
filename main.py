import platform
import os
import time

def block_websites(hosts_path, redirect, website_list):
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(f"{redirect} {website}\n")

def unblock_websites(hosts_path, website_list):
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def main():
    if platform.system() != 'Windows':
        print("This script is intended for Windows.")
        return

    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'
    website_list = ['www.example.com', 'www.blocked-site.com']

    while True:
        print("\nOptions:")
        print("1. Block Websites")
        print("2. Unblock Websites")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            block_websites(hosts_path, redirect, website_list)
            print("Websites blocked.")
        elif choice == '2':
            unblock_websites(hosts_path, website_list)
            print("Websites unblocked.")
        elif choice == '3':
            print("Exiting the Website Blocker Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
