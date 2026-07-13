from abbreviation import generate_platform_id
from length_enhancer import enhance_length
from structure_generator import generate_password
import sys

def main():
    print("██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗\n" 
            "██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗\n"
            "██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║\n"
            "██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║\n"
            "██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝\n"
            "╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝\n"
            "\n███████╗███╗   ██╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗███████╗\n"
            "██╔════╝████╗  ██║██║  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝\n"
            "█████╗  ██╔██╗ ██║███████║███████║██╔██╗ ██║██║     █████╗ \n"
            "██╔══╝  ██║╚██╗██║██╔══██║██╔══██║██║╚██╗██║██║     ██╔══╝ \n"
            "███████╗██║ ╚████║██║  ██║██║  ██║██║ ╚████║╚██████╗███████╗\n"
            "╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝\n"
          "\n===Welcome to Password Enhancement Framework===\n"
          )

    while True:

        print("\nMENU\n"
              "1. Check the introduction and rules\n"
              "2. Generate New Password\n"
              "3. View Password History\n"
              "E. Exit"
              )
        choice = input("Select: ").lower()

        if choice == "1":
            rule_display()
        elif choice == "2":
            generate_new_password()
        elif choice == "3":
            print("Coming soon...")
        elif choice == "e":
            print("\nGoodbye!")
            break

        else:
            print("\n! Invalid option !\n")

def rule_display():
    print("This Password Enhancement platform is aim to create strong and easy to memory password by our own algorithm.\n "
          "\nWhen user try to create a new password, the platform will request user to give below information:\n"
          "The User Name (can be real name)\n"
          "The Name of The Registered Platform (The entire process of the input platform will automatically become an abbreviation)\n"
          "A Year That Leaves A Deep Impression (Recommendation does not use  birthdays but the year when registered)\n "
          "\nAt the same time, the platform will remember all password that created when the platform is running until stop")
    back_or_exit()

def generate_new_password():
    # Remove the spaces entered by the user when entering the name
    name = "".join(input("\n================================\nEnter The Name: ").split())
    platform = input("Enter Registered Platform Name: ").strip()
    anchor = input("Enter Deep Impression Year ").strip()

    platform_id = generate_platform_id(platform)
    elements = [name, platform_id, anchor]
    enhanced_elements = enhance_length(elements)

    password = generate_password(enhanced_elements)
    print(f"\n================================\nYour new strong password is: {password}")
    back_or_exit()


def back_or_exit():

    while True:
        choice = input("\n================================\n[B] Back to Menu | [E] Exit : ").strip().lower()

        if choice == "b":
            return
        elif choice == "e":
            print("\nGoodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter B or E.")

if __name__ == "__main__":
    main()