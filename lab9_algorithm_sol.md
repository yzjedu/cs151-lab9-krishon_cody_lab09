# Algorithm for the Dinner Party Organizer Program

### Global Constant
- **`SEATS_PER_TABLE`**: Defines the number of seats available per table. Set globally to ensure all functions use the same constant value.

---

### Algorithm for `read_filename`
- **Purpose**: Prompt the user to input a filename and ensure the file exists. If not, keep prompting the user until a valid file is provided or the user opts to quit.
- **Name**: `read_filename`
- **Parameters**: None
- **Return**: The valid filename entered by the user, or `'quit'` if the user chooses to exit.
- **Algorithm**:
  1. Prompt the user to input the filename or type `'quit'` to exit.
  2. While the input is not `'quit'` and the file does not exist:
      1. Display an error message indicating the file does not exist.
      2. Prompt the user to input the filename again.
  3. Return the valid filename or `'quit'`.

---

### Algorithm for `read_names`
- **Purpose**: Read the names of attendees from the provided file.
- **Name**: `read_names`
- **Parameters**: `file_name` (string) - The name of the file containing attendees' names.
- **Return**: A list of names read from the file.
- **Algorithm**:
  1. Attempt to open the file in read mode.
  2. If the file is opened successfully:
      1. Create an empty list to store names.
      2. For each line in the file:
          - Strip any leading/trailing whitespace and append the name to the list.
      3. Return the list of names.
  3. If the file cannot be opened:
      - Display an error message and return an empty list.

---


### Algorithm for `display_seating`
- **Purpose**: Display the seating arrangement for attendees.
- **Name**: `display_seating`
- **Parameters**: `names` (list) - A list of attendees' names.
- **Return**: None
- **Algorithm**:
  1. Initialize variables `table = 1` and `seat = 1`.
  1. For each name in the `names` list:
      1. Print the table number, seat number, and attendee name in the desired format.
      2. Increment the seat number by 1.
      3. If `seat > SEATS_PER_TABLE`:
          - Increment the table number by 1.
          - Reset `seat` to 1.

---

### Algorithm for `main`
- **Purpose**: Main function to run the Dinner Party Organizer program.
- **Name**: `main`
- **Parameters**: None
- **Return**: None
- **Algorithm**:
  1. Display a welcome message explaining the purpose of the program.
  2. Call `read_filename()` to prompt the user for a filename.
  3. If the user enters `'quit'`:
      - Display a goodbye message and terminate the program.
  4. Call `read_names()` with the provided filename to retrieve the names.
  5. If the list of names is empty:
      - Display a message indicating that the file is empty.
  6. Otherwise:
      1. Display the total number of attendees.
      2. Calculate and display the total number of tables needed using `calculate_tables()`.
      3. Call `display_seating()` to display the seating arrangement.
  7. End the program with a thank-you message.