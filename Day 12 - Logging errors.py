import logging # module
import os

# Get the folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build path for errors.log inside that same folder
log_file = os.path.join(script_dir, "errors.log")

# Configure logging to always write in that file
logging.basicConfig(filename=log_file, level=logging.ERROR)

# Force reconfigure logging properly
# for handler in logging.root.handlers[:]:
#     logging.root.removeHandler(handler)

# Just save errors in a file called errors.log
# logging.basicConfig(filename="errors.log", level=logging.ERROR)

# basicConfig is a function from the logging module.
# When you call it, you are configuring the logging system (like setting up how your diary/log should look).
# Not a class or object itself — it’s just a setup function.

# logging.ERROR

# ERROR here is an attribute (constant value) inside the logging module.
# It represents a specific “logging level” (how serious the message is).
# Other attributes: logging.INFO, logging.DEBUG, etc.

# Attribute → Levels like ERROR or INFO (rules for what kind of notes you’ll write in the diary).

def get_number():
    try:
        num = int(input("Enter a number:"))
        print("You entered:", num)
    except ValueError as e: 
        # The "as e" part means - Store the error message inside a variable named e so I can use it later.
        # So e will contain something like:
        # invalid literal for int() with base 10: 'hello'
        print("Invalid input! Please enter a number.")
        logging.error(e)
        # logging.error(e)
        # This takes that technical error message (stored in e) and writes it into the log file (errors.log).
        # Example log entry:
        # ERROR:root:invalid literal for int() with base 10: 'hello'

# Run the program in a loop so user can try again
while True:
    get_number()

    # asking if user want to continur the input process
    choice = input("Do you want to continue(y/n): ")
    if choice.strip().lower() != "y":
        break

print("\n--- Program ended.")

# Ensure logs are written
logging.shutdown()