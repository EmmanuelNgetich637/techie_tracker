from developer_cli import developer_menu
from company_cli import company_menu
from project_cli import project_menu
from freebie_cli import freebie_menu
import sys

def main_menu():
    print("\n--- Techie Tracker CLI ---")
    print("1. Developers")
    print("2. Companies")
    print("3. Projects")
    print("4. Freebies")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            developer_menu()
        elif choice == "2":
            company_menu()
        elif choice == "3":
            project_menu()
        elif choice == "4":
            freebie_menu()
        elif choice == "5":
            print("Exiting... 👋")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
