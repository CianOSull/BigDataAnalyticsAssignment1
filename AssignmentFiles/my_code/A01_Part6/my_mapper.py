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
import bisect

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We get the parameter list from the line
    params_list = line.strip().split(",")

    #(00) start_time => A String representing the time the trip started at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:05:00”
    #(01) stop_time => A String representing the time the trip finished at <%d/%m/%Y %H:%M:%S>. Example: “2019/05/02 10:10:00”
    #(02) trip_duration => An Integer representing the duration of the trip. Example: 300
    #(03) start_station_id => An Integer representing the ID of the CityBike station the trip started from. Example: 150
    #(04) start_station_name => A String representing the name of the CitiBike station the trip started from. Example: “E 2 St &; Avenue C”.
    #(05) start_station_latitude => A Float representing the latitude of the CitiBike station the trip started from. Example: 40.7208736
    #(06) start_station_longitude => A Float representing the longitude of the CitiBike station the trip started from. Example:  -73.98085795
    #(07) stop_station_id => An Integer representing the ID of the CityBike station the trip stopped at. Example: 150
    #(08) stop_station_name => A String representing the name of the CitiBike station the trip stopped at. Example: “E 2 St &; Avenue C”.
    #(09) stop_station_latitude => A Float representing the latitude of the CitiBike station the trip stopped at. Example: 40.7208736
    #(10) stop_station_longitude => A Float representing the longitude of the CitiBike station the trip stopped at. Example:  -73.98085795
    #(11) bike_id => An Integer representing the id of the bike used in the trip. Example:  33882
    #(12) user_type => A String representing the type of user using the bike (it can be either “Subscriber” or “Customer”). Example: “Subscriber”.
    #(13) birth_year => An Integer representing the birth year of the user using the bike. Example:  1990
    #(14) gender => An Integer representing the gender of the user using the bike (it can be either 0 => Unknown; 1 => male; 2 => female). Example:  2.
    #(15) trip_id => An Integer representing the id of the trip. Example:  190

    # 3. If the list contains the right amount of parameters
    if (len(params_list) == 16):
        # 3.1. We set the right type for the parameters
        params_list[2] = int(params_list[2])
        params_list[3] = int(params_list[3])
        params_list[5] = float(params_list[5])
        params_list[6] = float(params_list[6])
        params_list[7] = int(params_list[7])
        params_list[9] = float(params_list[9])
        params_list[10] = float(params_list[10])
        params_list[11] = int(params_list[11])
        params_list[13] = int(params_list[13])
        params_list[14] = int(params_list[14])
        params_list[15] = int(params_list[15])

        # 3.2. We assign res
        res = tuple(params_list)

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
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
    res = "universal\t("

    # Using four lists to store the values because they can store duplicates.
    # Dictionaries can't store keys.
    first_station_names = []
    first_station_times = []

    second_station_names = []
    second_station_times = []

    # Set the previous varibles to be nothing by default
    prev_end_station_id = 0
    prev_end_station_log = 0
    prev_end_station_name = ""

    # For a line in that folder
    for line in my_input_stream:
        # Read all the attributes
        attributes = process_line(line)

        if attributes[11] == my_mapper_input_parameters[0]:
            # if previous station id is 0 then there isn't a previous station yet
            if (prev_end_station_id != 0) and (attributes[3] != prev_end_station_id):
                # Store station information in the dictioanry
                # Store the previous stations name as key and time as value
                first_station_names.append(prev_end_station_name)
                first_station_times.append(prev_end_station_log)

                # Store the current stations name as key and time as value
                second_station_names.append(attributes[4])
                second_station_times.append(attributes[0])

            prev_end_station_id = attributes[7]
            prev_end_station_name = attributes[8]
            prev_end_station_log = attributes[1]

    # Output the result
    # By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3,
    # station3_id) \n
    # if it is not empty, output
    if 0 < len(first_station_names):
        for i in range(len(first_station_names)):
            # By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3,
            # station3_id) \n
            # res = "universal\t(" + str(first_station_times[i]) + ", " + str(first_station_names[i]) + ", " + \
            #       str(second_station_times[i]) + ", " + str(second_station_names[i]) + ")\n"
            # print(res)

            res += str(first_station_times[i]) + " @ " + str(second_station_times[i]) + " @ " + str(first_station_names[i]) + " @ " + str(second_station_names[i])

        # Add the ) to the end
        res += ")"
        # print(res)

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
    file_name = "2019_05_10.csv"
    bike_id = 35143

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        file_name = sys.argv[1]

    # 2. Local or Hadoop
    local_False_hadoop_True = False

    # 3. We set the path to my_dataset and my_result
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout

    if (local_False_hadoop_True == False):
        my_input_stream = "../../my_dataset/" + file_name
        my_output_stream = "../../my_results/A01_Part6/1_my_map_simulation/" + file_name[:-4] + ".txt"

    # 4. my_mapper.py input parameters
    my_mapper_input_parameters = []
    my_mapper_input_parameters.append( bike_id )

    # 5. We call to my_main
    my_map(my_input_stream,
           my_output_stream,
           my_mapper_input_parameters
          )
