
import os

def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name



def read_file():
    f_name = read_file_name()
    fd = open(f_name, 'r')
    values = fd.readlines()
    fd.close()
    return values







