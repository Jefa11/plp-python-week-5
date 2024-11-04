def main():
    filename = "my_file.txt"

    try:
        with open(filename, 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is my first file.\n")
            file.write("The answer to life is 42.\n")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating the file: {e}")
    
    try:
        with open(filename, 'r') as file:
            print("\nContents of the file:")
            content = file.read()
            print(content)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")

    try:
        with open(filename, 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Another line added!\n")
            file.write("And yet another line with a number: 100.\n")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")

    try:
        with open(filename, 'r') as file:
            print("\nUpdated contents of the file after appending:")
            content = file.read()
            print(content)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file again: {e}")

if __name__ == "__main__":
    main()
