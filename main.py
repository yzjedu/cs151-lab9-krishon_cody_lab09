# Programmers:  [Krishon and Cody]
# Course:  CS151, [Professor Zee]
# Due Date: [11/14/2024]
# Lab Assignment:  [Lab 09]
# Problem Statement:  [Our program assigns seats and tables to people by reading a file with names]
# Data In: [the file they want to read from]
# Data Out:  [table and seat numbers for each person within the file]
# Credits: [class notes and class program]
# Input Files: [the input file 'read_file_name' asks user to input the file name and checks to see it it exists before proceeding]


# Import os package into the code
import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name


# Name: read_file
# Parameters: file_name
# Return: [], data
# Opens file from user input,tries to store file information into variable, except if file can't open then file is closed
def read_file(file_name):
    input_file = open(file_name, "r")
    try:
        data = input_file.readlines()
        input_file.close()
        return data
    except:
        input_file.close()
        print("File not found.")
        return[]

# Name: name_sign
# Parameters: file_name
# Return: [], name_list
# Stores information from in empty list, tries to open and file to return name_list,
# except if file can't open then file is closed and returns empty list
def name_sign(file_name):
    name_list = []
    open_file = open(file_name, "r")
    try:
        name_list = open_file.readlines()
        open_file.close()
        return name_list
    except:
        open_file.close()
        print("File not found.")
        return[]

# Purpose: to assign each person a table and seat
# Name: table_seating
# Parameters: filename
# Return: None
# Assigns each individual a table and seat, outputs information in format, and changes to new table when five seats are taken
def table_seating(file_name):
    tables = 1
    seat = 1
    for names in name_sign(file_name):
            print((f'{"~" * 20}\nTable{tables:<1}, Seat{seat:<1}, {names:<1}\n{"~" * 20:20}'))
            seat += 1
            if seat == 6:
                tables += 1
                seat = 1
    return

# Name: main
# Parameters: None
# Return: None
# Outputs the purpose of the program, assigns the invoked function read_file_name to a variable, file_name
# and invokes function name_sign and table_seating with argument, file_name.
def main():
    print('This program allows you to select a file that then assigns seats and tables to each name withing the file.\nFirst, select which file you want to read from.')
    file_name = read_file_name()
    name_sign(file_name)
    table_seating(file_name)

    return
# Invokes main function
main()







