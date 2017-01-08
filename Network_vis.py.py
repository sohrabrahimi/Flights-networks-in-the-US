import csv
import os
import glob
import math
import pandas
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from decimal import Decimal
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import networkx as nx
base = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)

G = nx.Graph()
os.chdir ("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges")
table = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/1991_2015.csv"
codes = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/airports_codes.csv"
Airloc = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/airport features/Airport_latlng.csv"
months = list(range(12,13))
years = list(range(2009,2016))
position = {}
with open (Airloc, "rb+") as table :
    reader = csv.reader(table)
    lst1 = []
    for i in reader :
        l = (i[0], [i[1],i[2]])
        lst1.append(l)
Dict_lst1 = dict(lst1)
print Dict_lst1.get("BWI")
list_pos= []

edges = []
for year in years:
    for month in months:
        os.chdir ("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges")
        with open ("1991_2015.csv", "rb+") as table2:
                reader = csv.reader(table2)
                count = 0
                edges = []
                for m in reader:
                  try:
                    if float(m[4])-float(year) == float(0):
                      if float(m[3]) - float(month) == float(0): 
                         if not float(m[2]) == 0.0:
                           edge = (m[1],math.pow(float(m[2]), 0.15))
                           edges.append(edge)
                           G.add_node(m[1], pos = (Dict_lst1.get(m[1])), air = 'dest')
                           G.add_node(m[0], pos = (Dict_lst1.get(m[0])), air = 'orig')
                           G.add_edge(m[0],m[1],weight = int(m[2]))
                  except: continue
            
        plt.figure(figsize=(5,5))
        pos=nx.get_node_attributes(G,'pos')
        lst_passeng = []
        lst_passeng2 = []
        lst_poses = []
        lst_pos2 = []
        count = -1
        for i in  pos.values():
          count = count+1
          try: 
            m = base(float(i[1]),float(i[0]))
            lst_poses.append(m)
            lst_pos2.append([pos.keys()[count],m])
          except:
              m == (0,0)
              lst_poses.append(m)
              lst_pos2.append((pos.keys()[count],m))
        kharreg = dict(lst_pos2)
        ##nodes,weights = zip(*nx.get_node_attributes(G,'passeng').items())
##        final_weights = []
##        dct =  nx.get_node_attributes(G,'air')
##        print dct
##        nod_weights = []
##        xxx = []
##        count = 0
##        for nod in nx.nodes(G): 
##            pas = 0
##            if dct.get(nod) == 'dest':
##                for nei in nx.all_neighbors(G,nod): 
##                     pas = pas + G[nei][nod]['weight']
##                edg = [nod,int(pas)]
##                xxx.append(edg)         
        ##    nod_weights.append((nod,pas))
##            if dct.get(nod) == 'orig':
##                for nei in nx.all_neighbors(G,nod): 
##                  if not edge in nx.non_edges(G):
##                     pas =0
##                edg2 = [nod,int(pas)]
##                xxx.append(edg2)
        os.chdir ("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/destinations")
        table2 = "C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/destinations/" + str(year)+"-"+ str(month)+".csv" 
        lats = []
        lons = []
        sizes = []
        dd = {}
        with open (table2, "rb+") as table2:
                reader = csv.reader(table2)
                for i in reader:
                   try: 
                    lats.append(float(Dict_lst1.get(i[0])[0]))
                    lons.append(float(Dict_lst1.get(i[0])[1]))
                    sizes.append(math.pow(float(i[1]), 0.6))
                   except: continue 
                    # aggregate passengers
                x, y = base(lons, lats)
                plt.figure(figsize = (30,30))
                nx.draw(G,kharreg,node_color='#ffa64d',node_size = 0 , alpha = 0.7, edge_color="#FFEBCD",width=0.15)
                base.scatter(x,y, s = sizes,c='#80ffff', marker = "o", alpha = 0.5 )
                base.bluemarble()
                plt.title(str(year)+"-"+str(month),color = 'black',horizontalalignment='left',verticalalignment = 'bottom', fontsize=60)
                os.chdir("C:/Users/sur216/Desktop/GISpython data/FLIGHTS/Domestic_monthly/edited_edges/images")
                plt.savefig(str(year)+"-"+str(month)+"_2.jpg")



