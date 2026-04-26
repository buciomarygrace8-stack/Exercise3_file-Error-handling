#Mary Grace Bucio

def main():
    try:
        username = input("Enter username: ").strip()
        
        if not username:
            raise ValueError("Username cannot be empty.")

        age_input = input("Enter age: ")
        age = int(age_input)

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        with open("users.txt", "w") as file:
            file.write(f"{username} - {age}\n")

        print("\nUser saved successfully.\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    try:
        print("\nSaved Users:")
        with open("users.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No users found. File does not exist yet.")

    finally:
        print("\nSystem complete.")


main()
