from abbreviation import generate_platform_id
from length_enhancer import enhance_length

def main():
    print("=== Password Enhancement Framework (BETA) ===")

    # Remove the spaces entered by the user when entering the name
    name = "".join(input("Enter your account name: ").split())
    platform = input("Enter the name of the platform you register for: ").strip()
    anchor = input("Enter memory anchor (e.g. the year you register in): ").strip()

    platform_id = generate_platform_id(platform)
    elements = [name, platform_id, anchor]
    enhanced_elements = enhance_length(elements)

    print("\nUser Input (TEST DATA)")
    print(f"Account name: {name}")
    print(f"Platform: {platform}")
    print(f"Platform ID (abbreviation): {platform_id}")
    print(f"Memory Anchor: {anchor}")
    print(f"Enhanced Elements: {enhanced_elements}")

if __name__ == "__main__":
    main()