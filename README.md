# BigDataAnalyticsAssignment1
First Assignment in Big Data Analytics Module.

Description:
Used Map Reduce Techniques in Python.

# BigDataAnalyticsAssignment2
 Second Project for Big Data Analytics module.<br />
 
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
