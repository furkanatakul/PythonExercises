import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
# Stack Plot
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]


plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol Sayısı")
plt.legend()
plt.show()

"""


""" 
Pie Grafiği

goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()


"""
""" 
Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
"""

"""
Histogram 
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")
"""
# x =[1,2,3,4]
# y=[1,4,9,16]
# plt.axis([0,6,0,20])
# plt.title("Grafik Başlığı")
# plt.xlabel("xlabel")
# plt.ylabel("ylabel")

# plt.plot(x,y,color="red",linewidth=2,marker="*")
# df = pd.read_csv("Datasets/GBvideos.csv")
# df["tag_count"] = df["tags"].str.split("|").apply(len)
# df = df["tag_count"]
# df.plot(subplots=True)
# plt.legend()

# x =np.linspace(-10,9,20)
# z= x**(1/5)
# y= x**3
#
# figure = plt.figure()
# axes = figure.add_axes([0.1,0.1,0.85,0.7])
# axes.plot(x,y,"--b")
# axes.plot(x,z,".r")
# axes.set_xlabel("Xlabel")
#
# axes2 = figure.add_axes([0.2,0.55,0.3,0.2])
# axes2.plot(x,z,".r")
# axes2.set_xlabel("xAxis")

fig, axes = plt.subplots(2,1)









plt.show()