from abbreviation import generate_platform_id

def main():
    # Use function "abbreviation" to get user input
    print("=== Password Enhancement Framework (BETA) ===")

    story = input("Enter your account name: ").strip()
    platform = input("Enter the name of the platform you register for (abbreviation or full name is acceptable): ").strip()
    anchor = input("Enter memory anchor (e.g. the year you register in): ").strip()

    platform_id = generate_platform_id(platform)

    # Test data show user input
    print("\nUser Input (TEST DATA)")
    print(f"Account name: {story}")
    print(f"Platform: {platform}")
    print(f"Platform ID (abbreviation): {platform_id}")
    print(f"Memory Anchor: {anchor}")


if __name__ == "__main__":
    main()