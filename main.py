from abbreviation import generate_platform_id
from length_enhancer import enhance_length
from structure_generator import generate_password

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

        print("MENU\n"
              "1. Generate New Password\n"
              "2. View Password History\n"
              "3. Exit"
              )
        choice = input("Select: ")

        if choice == "1":
            generate_new_password()
        elif choice == "2":
            print("Coming soon...")
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("\n! Invalid option !\n")

def generate_new_password():
    # Remove the spaces entered by the user when entering the name
    name = "".join(input("\nEnter your account name: ").split())
    platform = input("Enter the name of the platform you register for: ").strip()
    anchor = input("Enter memory anchor (e.g. the year you register in): ").strip()

    platform_id = generate_platform_id(platform)
    elements = [name, platform_id, anchor]
    enhanced_elements = enhance_length(elements)

    password = generate_password(enhanced_elements)
    print(f"\nYour new strong password is: {password}\n")

if __name__ == "__main__":
    main()