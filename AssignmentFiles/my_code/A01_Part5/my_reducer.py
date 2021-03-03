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

    # Split the line
    lines = line.strip().split("\t")

    # The station name
    bike_id = int(lines[1].split(", ")[0].strip("("))

    # Start station count
    # This line probably looks like mess but here is how it works.
    # First split e.g. '(24, 15)' into ['(24', '15)']
    # Then get the first index = '(24'
    # Then just remvoe the bracket
    duration = int(lines[1].split(", ")[1])

    # End station count
    trips = int(lines[1].split(", ")[2].strip(")"))

    res = (bike_id, duration, trips)

    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # NOTE FOR MYSELF:
    # The point of this is to go through each file and get the grand total for each street

    res = ""

    # Create a dictionary to store the top n bikes
    bike_id_duration = {}
    bike_id_trips = {}

    # For a line in that folder
    for line in my_input_stream:
        (bike_id, duration, trips) = process_line(line)
        # print(bike_id, duration, trips)

        # Add duration
        if bike_id in bike_id_duration:
            bike_id_duration[bike_id] += duration
        else:
            bike_id_duration[bike_id] = duration

        # Add trips
        if bike_id in bike_id_trips:
            bike_id_trips[bike_id] += trips
        else:
            bike_id_trips[bike_id] = trips

    # Sort hte duration by total duration
    sorted_duration = sorted(bike_id_duration.items(), key=lambda x: x[1], reverse=True)

    # Output the result for the top n bikes (write n amount of lines)
    # bike_id \t (total_duration_time_for_their_trips, total_number_of_trips) \n
    for i in range(my_reducer_input_parameters[0]):
        # This looks messy but it makes sense
        # sorted_duration[i][0] = the 0 index of a tuple in sorted duration is its bike id
        # sorted_duration[i][1] = the 1 index of a tuple in sorted duration is its total duration
        res = str(sorted_duration[i][0]) + "\t(" + str(sorted_duration[i][1]) + ", " + str(
            bike_id_trips[sorted_duration[i][0]]) + ")\n"

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
    top_n_bikes = 10

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        file_name = sys.argv[1]

    # 2. Local or Hadoop
    local_False_hadoop_True = False

    # 3. We set the path to my_dataset and my_result
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout

    if (local_False_hadoop_True == False):
        my_input_stream = "../../my_results/A01_Part5/2_my_sort_simulation/" + file_name
        my_output_stream = "../../my_results/A01_Part5/3_my_reduce_simulation/reduce_" + file_name[5:]

    # 4. my_reducer.py input parameters
    my_reducer_input_parameters = []
    my_reducer_input_parameters.append( top_n_bikes )

    # 5. We call to my_main
    my_map(my_input_stream, my_output_stream, my_reducer_input_parameters)
