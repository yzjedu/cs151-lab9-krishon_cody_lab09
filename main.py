




import os

def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name



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


def table_seating(filename):
    tables = 1
    seat = 1
    for names in name_sign(filename):
            seat_chart = print(f'{"~" * 20}\nTable{tables:<1}, Seat{seat:<1}, {names:<1}\n{"~" * 20}')
            seat += 1
            if seat == 6:
                tables += 1
                seat = 1
    print(seat_chart)
    return




def main():
    filename = read_file_name()
    #names = read_file(filename)
    name_sign(filename)
    table_seating(filename)

    return

main()







