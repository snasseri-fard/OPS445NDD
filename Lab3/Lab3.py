### Lab3: A function that will write a text file to your PC with your name

def write_text_file_with_name():
    name = input("Enter your name: ")

    # Open the file in write mode
    with open("output.txt", "w") as file:
        # Write the name to the file
        file.write(name)

    print("File created successfully.")

# Example usage:
write_text_file_with_name()

