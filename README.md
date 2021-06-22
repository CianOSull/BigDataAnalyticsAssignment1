# BigDataAnalyticsAssignment1
First Assignment in Big Data Analytics Module.<br /> 

Description:<br /> 
Used Map Reduce Techniques in Python.<br /> 

Code is located AssignmentFiles -> my_code
 
## Project specifiction:<br />
**Tasks**:<br />
o A01_Part1/A01_Part1.py<br />
o A01_Part2/A01_Part2.py<br />
o A01_Part3/A01_Part3.py<br />
Complete the function my_main of the Python program.<br />
Do not modify the name of the function nor the parameters it receives.<br />
o A01_Part4/my_mapper.py<br />
o A01_Part5/my_mapper.py<br />
o A01_Part6/my_mapper.py<br />
Complete the function my_map of the Python program.<br />
Do not modify the name of the function nor the parameters it receives.<br />
o A01_Part4/my_reducer.py<br />
o A01_Part5/my_reducer.py<br />
o A01_Part6/my_reducer.py<br />
Complete the function my_reduce of the Python program.<br />
Do not modify the name of the function nor the parameters it receives<br />

**Task 1**:<br />
Technology:<br />
Python (without using the MapReduce simulator).<br />
<br />
Your task is to:<br />
• Compute the amount of trips starting from and finishing at each station_name.<br /> 
<br />
_Complete the function my_main of the Python program._<br />
o Do not modify the name of the function nor the parameters it receives.<br />
o In particular, the function must read the dataset provided in input_folder and must open and write the results to output_file. <br />
o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
Results:<br />
Output one text line per station_name. Lines must follow alphabetic order in the name of the station. Each line must have the following format: <br /> 
station_name \t (total_trips_starting_from_the_station, total_trips_finishing_at_the_station) \n<br />

**Task 2**:<br />
Technology:<br />
Python (without using the MapReduce simulator) <br />
<br />
Your task is to:<br />
• Compute the top_n_bikes with highest total duration time for their trips <br /> 
<br />
_Complete the function my_main of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the dataset provided in input_folder and must open and write the results to output_file. The number of bikes to output is specified by the parameter top_n_bikes. For example, if top_n_bikes = 10, then you must output the 10 bikes with highest total duration time for their trips. <br />
o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
Results:<br />
Output one text line per bike_id. Lines must follow decreasing order in highest total duration time for their trips. Each line must have the following format: <br />
bike_id \t (total_duration_time_for_their_trips, total_number_of_trips) \n <br />

**Task 3**:<br />
Technology:<br />
Python (without using the MapReduce simulator) <br />
<br />
Your task is to:<br />
• Sometimes bikes are re-organised (moved) from station A to station B to balance the amount of bikes available in both stations. A truck operates this bike re-balancing service, and the trips done by-truck are not logged into the dataset. Compute all the times a given bike_id was moved by the truck re-balancing system <br />
<br />
_Complete the function my_main of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the dataset provided in input_folder and must open and write the results to output_file. The concrete bike to be tracked is specified by the parameter bike_id. For example, if bike_id = 35143, then you must track all the times the bike with id 35143 was moved by the truck re-balancing system. o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
Results:<br />
Output one text line per moving trip. Lines must follow temporal order. Each line must have the following format: <br />
By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3, station3_id) \n <br />
For example, if the dataset contains the following 2 trips: <br />
o Trip1: A user used bike_id to start a trip from Station1 on 2019/05/10 09:00:00 and finished the trip at Station2 on 2019/05/10 10:00:00 <br />
o Trip2: A user used bike_id to start a trip from Station3 on 2019/05/10 11:00:00 and finished the trip at Station4 on 2019/05/10 12:00:00 <br />
<br />
And the dataset does not contain any extra trip: <br />
o Trip3: A user used bike_id to start a trip from Station2 and finish at Station3 anytime between 2019/05/10 10:00:00 and 2019/05/10 11:00:00 <br />
Then it is clear that the bike was moved from Station2 to Station3 by truck, and we output: <br />
By_Truck \t (2019/05/10 10:00:00, Station2, 2019/05/10 11:00:00, Station3) \n <br />

**Task 4**:<br />
Technology:<br />
Python - Use the MapReduce simulator. <br />
<br />
Your task is to: <br />
• Compute the amount of trips starting from and finishing at each station_name. <br /> 
<br />
_my_mapper.py => Complete the function my_map of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. There are no extra parameters provided via my_mapper_input_parameters. <br />
o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
_my_reducer.py => Complete the function my_reduce of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. There are no extra 
parameters provided via my_reducer_input_parameters. <br />
o You can also program any other auxiliary functions you might need. <br /> 
<br />
Results:<br />
Output one text line per station_name. Lines must follow alphabetic order in the name of the station. Each line must have the following format: <br />
station_name \t (total_trips_starting_from_the_station, total_trips_finishing_at_the_station) \n <br />

**Task 5**:<br />
Technology:<br />
Python - Use the MapReduce simulator. <br />
<br />
Your task is to: <br />
• Compute the top_n_bikes with highest total duration time for their trips. <br /> 
<br />
_my_mapper.py => Complete the function my_map of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. There are no extra parameters provided via my_mapper_input_parameters. <br />
o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
_my_reducer.py => Complete the function my_reduce of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br />
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. The extra parameter top_n_bikes is provided via my_reducer_input_parameters. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
Results:<br />
Output one text line per bike_id. Lines must follow decreasing order in highest total duration time for their trips. Each line must have the following format: <br />
bike_id \t (total_duration_time_for_their_trips, total_number_of_trips) \n <br />

**Task 6**:<br />
Technology:<br />
Python - Use the MapReduce simulator. <br />
<br />
Your task is to: <br />
• Sometimes bikes are re-organised (moved) from station A to station B to balance the amount of bikes available in both stations. A truck operates this bike re-balancingservice, and the trips done by-truck are not logged into the dataset. Compute all the times a given bike_id was moved by the truck re-balancing system. <br /> 
<br />
_my_mapper.py => Complete the function my_map of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives.
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. The extra parameter bike_id is provided via my_mapper_input_parameters. <br />
o You can use the auxiliary function process_line which, given one line from a dataset file, returns a tuple with its content. <br />
o You can also program any other auxiliary functions you might need. <br />
<br />
_my_reducer.py => Complete the function my_reduce of the Python program._ <br />
o Do not modify the name of the function nor the parameters it receives. <br /> 
o In particular, the function must read the content of a file provided by my_input_stream and must write the results to the file provided by my_output_stream. There are no extra parameters provided via my_reducer_input_parameters. <br /> 
o You can also program any other auxiliary functions you might need. <br /> 
<br />
Results:<br />
Output one text line per moving trip. Lines must follow temporal order. Each line must have the following format: <br /> 
By_Truck \t (time_it_was_logged_at_station2, station2_id, time_it_was_logged_at_station3, station3_id) \n <br /> 
For example, if the dataset contains the following 2 trips: <br /> 
o Trip1: A user used bike_id to start a trip from Station1 on 2019/05/10 09:00:00 and finished the trip at Station2 on 2019/05/10 10:00:00 <br /> 
o Trip2: A user used bike_id to start a trip from Station3 on 2019/05/10 11:00:00 and finished the trip at Station4 on 2019/05/10 12:00:00And the dataset does not contain any extra trip: <br /> 
o Trip3: A user used bike_id to start a trip from Station2 and finish at Station3 anytime between 2019/05/10 10:00:00 and 2019/05/10 11:00:00 <br /> 
<br /> 
Then it is clear that the bike was moved from Station2 to Station3 by truck, and we output: <br /> 
By_Truck \t (2019/05/10 10:00:00, Station2, 2019/05/10 11:00:00, Station3) \n <br /> 

**Dataset Information:**<br />
This dataset occupies ~80MB and contains 73 files. Each file contains all the trips 
registered the CitiBike system for a concrete day:<br />
• 2019_05_01.csv => All trips registered on the 1st of May of 2019. <br />
• 2019_05_02.csv => All trips registered on the 2nd of May of 2019. <br />
• 2019_07_12.csv => All trips registered on the 12th of July of 2019.<br />
<br />
Altogether, the files contain 444,110 rows. Each row contains the following fields:<br />
start_time , stop_time , trip_duration , start_station_id , start_station_name , 
start_station_latitude , start_station_longitude , stop_station_id , stop_station_name , 
stop_station_latitude , stop_station_longitude , bike_id , user_type , birth_year , gender , 
trip_id<br />
<br />
• (00) start_time<br />
! A String representing the time the trip started at. <br />
<%Y/%m/%d %H:%M:%S> <br />
! Example: “2019/05/02 10:05:00”<br />
• (01) stop_time<br />
! A String representing the time the trip finished at. <br />
<%Y/%m/%d %H:%M:%S> <br />
! Example: “2019/05/02 10:10:00”<br />
• (02) trip_duration<br />
! An Integer representing the duration of the trip.<br />
! Example: 300<br />
• (03) start_station_id<br />
! An Integer representing the ID of the CityBike station the trip started from.<br />
! Example: 150<br />
• (04) start_station_name<br />
! A String representing the name of the CitiBike station the trip started from.<br />
! Example: “E 2 St &; Avenue C”.<br />
• (05) start_station_latitude<br />
! A Float representing the latitude of the CitiBike station the trip started from.<br />
! Example: 40.7208736<br />
• (06) start_station_longitude<br />
! A Float representing the longitude of the CitiBike station the trip started from.<br />
! Example: -73.98085795<br />
• (07) stop_station_id<br />
! An Integer representing the ID of the CityBike station the trip stopped at.<br />
! Example: 150<br />
• (08) stop_station_name! A String representing the name of the CitiBike station the trip stopped at. <br />
! Example: “E 2 St &; Avenue C”.<br />
• (09) stop_station_latitude<br />
! A Float representing the latitude of the CitiBike station the trip stopped at.<br />
! Example: 40.7208736<br />
• (10) stop_station_longitude<br />
! A Float representing the longitude of the CitiBike station the trip stopped at.<br />
! Example: -73.98085795<br />
• (11) bike_id<br />
! An Integer representing the id of the bike used in the trip. <br />
! Example: 33882.<br />
• (12) user_type<br />
! A String representing the type of user using the bike (it can be either “Subscriber” <br />
or “Customer”). <br />
! Example: “Subscriber”.<br />
• (13) birth_year<br />
! An Integer representing the birth year of the user using the bike. <br />
! Example: 1990.<br />
• (14) gender<br />
! An Integer representing the gender of the user using the bike (it can be either 0 => <br />
Unknown; 1 => male; 2 => female).<br />
! Example: 2.<br />
• (15) trip_id<br />
! An Integer representing the id of the trip. <br />
! Example: 190.<br />
