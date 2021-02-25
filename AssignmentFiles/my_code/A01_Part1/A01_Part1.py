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
def my_main(input_folder, output_file):
    # Task:
    # Compute the amount of trips starting from each station_name.
    # Compute the amount of trips finishing at each station_name.
    # Key information:
    # (04) start_station_name
    # (08) stop_station_name

    # This will be a string for you outputting
    # Ouput should be:
    # station_name \t (total_trips_starting_from_the_station, total_trips_finishing_at_the_station) \n
    # Lines should be in alphebetical order and one line  each
    res = ""

    # This dictionary will store all the start stations
    start_stations = {}

    # This will store the end stations
    end_stations = {}

    # File names for each file in the input folder
    data_filename = os.listdir(input_folder)

    # For a file in the input folder
    for filename in data_filename:
        # Open the file
        data_file = open(input_folder + "\\" + filename, "r")

        # For a line in that folder
        for line in data_file.readlines():
            # Read all the attributes
            attributes = process_line(line)

            # Increase the count of the start station
            if attributes[4] in start_stations:
                start_stations[attributes[4]] += 1
            else:
                start_stations[attributes[4]] = 1

            # Increase the count of the end station
            if attributes[8] in end_stations:
                end_stations[attributes[8]] += 1
            else:
                end_stations[attributes[8]] = 1

        # Close the file
        data_file.close()

    # This will be a list of all the unique station names
    all_stations_sorted = list(set(start_stations.keys()).union(set(end_stations.keys())))
    # Sort the list
    all_stations_sorted.sort()

    # Delete the ouput fiel if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    for station_name in all_stations_sorted:
        # Open the outfile
        output = open(output_file, "a")

        # This if block checks to make sure that each station name is in both dicitonaries
        if (station_name in start_stations) and (station_name in end_stations):
            # Create the output line
            res = station_name + "\t(" + str(start_stations[station_name]) + ", " + str(end_stations[station_name]) + ") \n"

        elif station_name in start_stations:
            res = station_name + "\t(" + str(start_stations[station_name]) + ", 0) \n"

        elif station_name in end_stations:
            res = station_name + "\t(0, " + str(end_stations[station_name]) + ") \n"

        # # Print the result
        # print(res)

        # Output to file
        output.write(res)
        
        # Close output file
        output.close()


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
    output_file = "../../my_results/A01_Part1/result.txt"

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):
        input_folder = sys.argv[1]
        output_file = sys.argv[2]

    # 2. We call to my_main
    my_main(input_folder, output_file)
