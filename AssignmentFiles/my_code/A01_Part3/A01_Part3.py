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
import os
import codecs
import sys
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
# FUNCTION my_main
# ------------------------------------------
def my_main(input_folder, output_file, bike_id):
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

    # File names for each file in the input folder
    data_filename = os.listdir(input_folder)

    # This will previous store the station name as the key and the log time as the value
    # first_station_info = {}

    # This will current store the station name as the key and the log time as the value
    # second_station_info = {}

    # Create lists of the keys and values to make it easier to print htem at once
    first_station_names = []
    first_station_times = []

    second_station_names = []
    second_station_times = []

    # Set hte previous varibles to be nothing by default
    prev_end_station_id = 0
    prev_end_station_log = 0
    prev_end_station_name = ""

    # For a file in the input folder
    for filename in data_filename:
        # Open the file
        data_file = open(input_folder + filename, "r")

        # For a line in that folder
        for line in data_file.readlines():
            # Read all the attributes
            attributes = process_line(line)

            if attributes[11] == bike_id:
                # if previous station id is 0 then there isn't a previous station yet
                if (prev_end_station_id != 0) and (attributes[3] != prev_end_station_id):
                    # Store station information in the dictioanry
                    # Store the previous stations name as key and time as value
                    # first_station_info[prev_end_station_name] = prev_end_station_log
                    first_station_names.append(prev_end_station_name)
                    first_station_times.append(prev_end_station_log)
                    
                    # Store the current stations name as key and time as value
                    # second_station_info[attributes[4]] = attributes[0]
                    second_station_names.append(attributes[4])
                    second_station_times.append(attributes[0])

                    # print("Truck was used:")
                    # print("Previous end station:", prev_end_station_id)
                    # print("Previous end station time:", prev_end_station_log)
                    # print("New start station:", attributes[3])
                    # print("New start station time:", attributes[0])

                prev_end_station_id = attributes[7]
                prev_end_station_name = attributes[8]
                prev_end_station_log = attributes[1]

        # Close the file
        data_file.close()

    # Delete the output file if it exists
    # if os.path.exists(output_file):
    #     os.remove(output_file)

    # Create lists of the keys and values to make it easier to print htem at once
    # first_station_names = list(first_station_info.keys())
    # first_station_times = list(first_station_info.values())
    # 
    # second_station_names = list(second_station_info.keys())
    # second_station_times = list(second_station_info.values())

    # Output the result
    # By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3,
    # station3_id) \n
    # Second maybe output?
    # By_Truck \t (2019/05/10 10:00:00, Station2, 2019/05/10 11:00:00, Station3) \n
    for i in range(len(first_station_names)):
        # Open the outfile
        # output = open(output_file, "a")

        # By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3,
        # station3_id) \n
        res = "By_Truck \t(" + str(first_station_times[i]) + ", " + str(first_station_names[i]) + ", " + \
              str(second_station_times[i]) + ", " + str(second_station_names[i]) + ")\n"
        print(res)

        # Output to file
        # output.write(res)

        # Close output file
        # output.close()

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    input_folder = "../../my_dataset/"
    output_file = "../../my_results/A01_Part3/result.txt"
    bike_id = 35143

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        input_folder = sys.argv[1]
        output_file = sys.argv[2]

    # 2. We call to my_main
    my_main(input_folder, output_file, bike_id)
