### Lab2: A function that uses command line arguments. This function will print two variables used, the script and then the script AND variables.

import sys

def print_arguments():
    # Get the script name
    script_name = sys.argv[0]

    # Print the script name
    print("Script name:", script_name)

    # Check if any arguments were passed
    if len(sys.argv) > 1:
        # Print the script name and variables
        print("Script name and variables:", " ".join(sys.argv))

# Example usage:
print_arguments()

def helloWorld():
	print(‘Hello World’)

helloWorld()
