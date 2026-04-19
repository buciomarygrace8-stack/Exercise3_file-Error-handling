filename = "notes.txt"

try:
    note = input("Enter a short note/message: ")
    with open(filename, "w") as file:
        file.write(note + "\n")
    print("\nMessage saved successfully!\n")
except Exception as e:
    print("Error writing to file:", e)


try:
    print("Reading file content:")
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error reading file:", e)


try:
    new_note = input("\nEnter another note to append: ")
    with open(filename, "a") as file:
        file.write(new_note + "\n")

    print("\nUpdated file content:")
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error appending to file:", e)