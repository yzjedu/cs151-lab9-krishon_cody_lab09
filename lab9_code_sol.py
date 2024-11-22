import os

SEATS_PER_TABLE = 5
# Function: read_filename
# Purpose: Prompts the user for a filename and ensures the file exists.
# Parameters: None
# Return: str - The valid filename entered by the user or 'quit' if the user chooses to exit.
def read_filename():
    name = input("What file do you want to read? (or type 'quit' to exit): ").lower().strip()
    while name != 'quit' and not os.path.isfile(name):
        print("That file does not exist. Please try again.")
        name = input("What file do you want to read? (or type 'quit' to exit): ").strip()
    return name

# Function: read_names
# Purpose: Reads names from the given file.
# Parameters: file_name (str) - The name of the file to read.
# Return: list - A list of names read from the file.
def read_names(file_name):
    try:
        file = open(file_name, 'r')
        names = []
        for line in file:
            names.append(line.strip())
        return names
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

# Purpose: Displays the seating arrangement for the attendees.
# Parameters: names (list) - A list of attendees' names.
# Return: None
def display_seating(names):
    table = 1
    seat = 1
    for name in names:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Table {table}, Seat {seat}, {name}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        seat += 1
        if seat > SEATS_PER_TABLE:
            table += 1
            seat = 1

# Function: main
# Purpose: Main function to run the Dinner Party Organizer.
# Parameters: None
# Return: None
def main():
    print()
    print("Welcome to the Dinner Party Organizer!")
    print("This program will calculate the seating arrangement for the attendees.")
    print()
    file_name = read_filename()
    if file_name.lower() == 'quit':
        print("Thank you for using the Dinner Party Organizer. Goodbye!")
        return

    names = read_names(file_name)
    if len(names) == 0:
        print("The file is empty. No attendees to organize.")
    else:
        print(f"\nTotal Attendees: {len(names)}")
        print(f"Total Tables Needed: {len(names)  // SEATS_PER_TABLE}")
        print("\nSeating Arrangement:")
        display_seating(names)

main()