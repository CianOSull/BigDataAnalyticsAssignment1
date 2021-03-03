#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # The return tuple
    res = ()

    # Split the line into its individual components
    # line_info will look something like this:
    # ['(2019/05/07 11:42:00', 'Banker St & Meserole Ave', '2019/05/07 15:57:14', 'Norfolk St & Broome St)']
    # line_info = line.strip().split("\t")[1].split(", ")
    # first_time = line_info[0].strip("(")
    # first_name = line_info[1]
    # second_time = line_info[2]
    # second_name = line_info[3].strip(")")

    # New order looks like this:
    # (first time @ second time @ first station @ second station)
    # line_info = line.strip().split("\t")[1].split(" @ ")
    line_info = line.strip().split("\t")[1].split(" @ ")

    first_time = line_info[0].strip("(")
    second_time = line_info[1]
    first_name = line_info[2]
    second_name = line_info[3].strip(")")

    # print(first_time, second_time, first_name, second_name)
    res = (first_time, second_time, first_name, second_name)

    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # Task:
    # Sometimes bikes are re-organised (moved) from station A to station B to balance the
    # amount of bikes available in both stations. A truck operates this bike re-balancing
    # service, and the trips done by-truck are not logged into the dataset. Compute all the
    # times a given bike_id was moved by the truck re-balancing system.

    # (03) start_station_id
    # (07) stop_station_id

    # (04) start_station_name
    # (08) stop_station_name

    # (01) stop_time

    # Output variable
    res = ""

    # For a line in that folder
    for line in my_input_stream:
        # This should only run if the length of line is more than 13 characters because if it is,
        # then that means there is information in the line. If iti s only 13 then it is blank
        (first_time, second_time, first_name, second_name) = process_line(line)

        # By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3,
        # station3_id) \n
        res = "By_Truck \t(" + first_time + ", " + first_name + ", " + \
              second_time + ", " + second_name + ")\n"

        # Output to file
        my_output_stream.write(res)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    file_name = "sort_1.txt"

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        file_name = sys.argv[1]

    # 2. Local or Hadoop
    local_False_hadoop_True = False

    # 3. We set the path to my_dataset and my_result
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout

    if (local_False_hadoop_True == False):
        my_input_stream = "../../my_results/A01_Part6/2_my_sort_simulation/" + file_name
        my_output_stream = "../../my_results/A01_Part6/3_my_reduce_simulation/reduce_" + file_name[5:]

    # 4. my_reducer.py input parameters
    my_reducer_input_parameters = []

    # 5. We call to my_main
    my_map(my_input_stream, my_output_stream, my_reducer_input_parameters)
