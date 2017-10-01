# Flights-networks-in-the-US

This project is intended to assist the Hershey Company to get a better understanding of the travel dynamics in the United States. Hershey company's marketting strategies rely heavily on event detection processes. Studying the flight networks is one way to find major events accross the US. 

In this study I will first visualize the network of flights in the past 10 years by creating Giff files which have been created in python. First I created a network of flights with NetworkX 2.7 package and then generated some maps illustrating this network. The code for this process can be found in Network_vis.py file.  Next I created an animation from the resulting images. The code for that process can be found in image2giff.py file. 

In order to find the potential events, I made times series of city-to-city flights and looked into sudden jummps in those time series using the peakutils 2.7. package in python. The code for that part can be found in time_series.py file. 
