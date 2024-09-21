# file_handling_assignment.py

# File Creation
try:
    # Create and open the file in write mode
    with open('my_file.txt', 'w') as file:
        # Write lines to the file
        file.write("This is the first line of text.\n")
        file.write("Here is the second line with a number: 42\n")
        file.write("Finally, this is the third line.\n")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while creating the file: {e}")

finally:
    print("File creation complete.")

# File Reading and Display
try:
    # Open the file in read mode
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File Contents:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

finally:
    print("File reading complete.")

# File Appending
try:
    # Open the file in append mode
    with open('my_file.txt', 'a') as file:
        # Append additional lines to the file
        file.write("This is an appended line one.\n")
        file.write("Another appended line, number: 100.\n")
        file.write("And the final appended line.\n")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")

finally:
    print("File appending complete.")

# Final reading to display the new contents
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Updated File Contents:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

finally:
    print("Final file reading complete.")
