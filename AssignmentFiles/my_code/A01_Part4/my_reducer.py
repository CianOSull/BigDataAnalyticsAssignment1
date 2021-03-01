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


def process_line(line):
    # The return tuple
    res = ()

    # Split the line
    lines = line.strip().split("\t")

    # The station name
    station = lines[0]

    # Start station count
    # This line probably looks like mess but here is how it works.
    # First split e.g. '(24, 15)' into ['(24', '15)']
    # Then get the first index = '(24'
    # Then just remvoe the bracket
    start_count = int(lines[1].split(", ")[0].strip("("))

    # End station count
    end_count = int(lines[1].split(", ")[1].strip(")"))

    res = (station, start_count, end_count)

    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # NOTE FOR MYSELF:
    # The point of this is to go through each file and get the grand total for each street

    res = ""

    start_station_dict = {}
    end_station_dict = {}

    for line in my_input_stream:
        # Set the values here
        (station, start_count, end_count) = process_line(line)
        if station in start_station_dict:
            start_station_dict[station] += start_count
        else:
            start_station_dict[station] = start_count

        if station in end_station_dict:
            end_station_dict[station] += end_count
        else:
            end_station_dict[station] = end_count

        # print(station, start_count, end_count)
        # print(start_count)
        # print(end_count)
        # print(start_station_dict)

    # This will be a list of all the unique station names
    all_stations_sorted = list(set(start_station_dict.keys()).union(set(end_station_dict.keys())))
    # Sort the list
    all_stations_sorted.sort()

    # The big change to this part is at the bottom, now it is using the output stream passed in to do outputting
    for station_name in all_stations_sorted:
        # This if block checks to make sure that each station name is in both dicitonaries
        if (station_name in start_station_dict) and (station_name in end_station_dict):
            # Create the output line
            res = station_name + "\t(" + str(start_station_dict[station_name]) + ", " + str(
                end_station_dict[station_name]) + ") \n"

        elif station_name in start_station_dict:
            res = station_name + "\t(" + str(start_station_dict[station_name]) + ", 0) \n"

        elif station_name in end_station_dict:
            res = station_name + "\t(0, " + str(end_station_dict[station_name]) + ") \n"

        # Using output stream passed to output
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
        my_input_stream = "../../my_results/A01_Part4/2_my_sort_simulation/" + file_name
        my_output_stream = "../../my_results/A01_Part4/3_my_reduce_simulation/reduce_" + file_name[5:]

    # 4. my_reducer.py input parameters
    my_reducer_input_parameters = []

    # 5. We call to my_main
    my_map(my_input_stream, my_output_stream, my_reducer_input_parameters)
