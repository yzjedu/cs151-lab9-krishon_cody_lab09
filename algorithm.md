# Algorithm Document


1. Import os
2. Function 1
    * Purpose: To read the file and make sure user enters a valid filed
    * Name: read_file_name
    * Parameters: None
    * Return: f_name
    * Algorithm:
      1. f_name = ask user to input the file name
      2. while not os.path.isfile(f_name):
         1. tell user the file doesn't exist, prompt to enter again under f_name
      3. Return f_name

3. Function 2
    * Purpose: To open and close the file and to read the lines in the file
    * Name: read_file
    * Parameters: file_name
    * Return: [], data
    * Algorithm:
      1. open the file for reading purpose, input_file
      2. try
         1. data = input_file.readlines()
         2. close the file
         3. return data
      3. except
         1. close the file
         2. output to user the file isn't found, 
         3. return []

4. Function 3
    * Purpose: To open and close the name list
    * Name: name_sign
    * Parameters: file_name
    * Return: [], name_list
    * Algorithm:
      1. name_list = []
      2. open the file for reading purpose, open_file
      3. try
         1. name_list = open_file.readlines()
         2. close the file
         3. return name_list
      4. except
         1. close the file
         2. output to the user the file isn't found
         3. return []

5. Function 4
    * Purpose: to assign each person a table and seat
    * Name: table_seating
    * Parameters: filename
    * Return: None
    * Algorithm:
      1. assign tables and seat equal to 1
      2. for names in name_sign(filename)
         1. seat_chart = print the table and seat for each person, separate with "~"
         2. seat += 1
         3. if seat == 6
            1. tables += 1
            2. seat = 1
      3. print(seat_chart)
      4. return

6. Function 5
    * Purpose: Running the entire program
    * Name: main
    * Parameters: None
    * Return: None
    * Algorithm:
      1. output the purpose of the program to the user
      2. filename = read_file_name()
      3. call name_sign(filename)
      4. call table_seating(filename)
      5. Return

7. Call main function