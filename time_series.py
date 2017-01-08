import os
import csv
import numpy as np
import peakutils
import itertools
import matplotlib.pyplot as plt
folder = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/destinations"
os.chdir(folder)
files = os.listdir(folder)
ap_date = {}
Airport = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/airport features/airport_cities.csv"
with open (Airport, "rb+") as table :
    reader = csv.reader(table)
    lst1 = []
    for i in reader :
        l = (i[0], i[1])
        lst1.append(l)
air_city = dict(lst1)
for i in files:
    name =  i.split(".")[0]
    table = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/destinations/"+i
    print "processing table", i
    with open (table,"rb+") as table:
       reader = csv.reader(table)
       for line in reader:
           if ap_date.get(line[0]) == None:
               ap_date[line[0]] = [{name:float(line[1])}]
           else:
               ap_date[line[0]] += [{name:float(line[1])}]
 
           
print ap_date["SCE"]
airps = ap_date.keys()
print airps
count = 0
os.chdir = ("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/graphs")
air_list = []
for i in airps:
    date_pass = ap_date.get(i)
    dates = []
    passengers = []
    for dp in date_pass:
        dates.append(dp.keys())
        passengers.append(dp.values())
##    fig = plt.figure(figsize=(12, 4), facecolor = 'white')
    x = list(range(len(dates)))
##    ymax = max([max(passen) for passen in passengers])* 1.05
##    xmax = max(x)* 1.05
##    plt.xlim(0,xmax)
##    plt.ylim(0,ymax)
##    plt.ylabel("Total Number of Passengers", fontsize = 8)
##    plt.xlabel("Year-month", fontsize = 8)
##    plt.xticks(x,dates, rotation = 90, fontsize = 2)
    y = passengers
##    try: 
##      plt.title("aggregated monthly passenger population for "+ i + " airport ( " + air_city.get(i) + " )", fontsize = 9, color = "blue")
##    except:
##      plt.title("aggregated monthly passenger population for "+ i + " airport" , fontsize = 10, color = "blue") 
    plt.plot(x,y)
    m_pass = []
    for p in passengers:
        for m in p:
            m_pass.append(m)
    cb = np.array(m_pass)
    indexes = peakutils.indexes(cb, thres = 0.0002/max(cb),min_dist = 1)
    peaks = []
    dict_month = {1:'Jan ', 2:'Feb ', 3:'Mar ', 4:'Apr ', 5:'May ', 6:'Jun ', 7:'Jul ', 8:'Aug ', 9:'Sep ', 10:'Oct ' , 11:'Nov ', 12:'Dec' }
    for w in indexes:
        for date in dates[w]:
          if not float(date.split("-")[0])>2010: continue
          d = str(date.split("-")[0]) + "-" + str(dict_month.get(int(date.split("-")[1])))
          peaks.append(d)
    tesso = 'The peak dates after 2010 for this airport are:'
    text = ','.join(peaks)
    plt.text
    air_list.append([i,[text]])
##    plt.savefig("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/graphs/"+str(i)+".jpg")
tt = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/graphs/peaks.csv"
with open (tt, "wb+") as tt:
        writer = csv.writer(tt)
        for air in air_list:
             writer.writerow(air)

    

