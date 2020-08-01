# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:15:44 2020

@author: HP PC
"""
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup=BeautifulSoup(webpage,'lxml')
body=soup.find_all('table',{'id':'main_table_countries_today'})[0]
len(body)

import csv
csv_file=open("coronavirus.csv","w",newline='')
csv_writer=csv.writer(csv_file)
data=[]
try:
    for i in body.find_all('tr'):
        data=[]
        for k in i.find_all(['th','td']):
            data.append(k.get_text())
        csv_writer.writerow(data)
finally:
    csv_file.close()



df=pd.read_csv("C:\\Users\\HP PC\\AI BOT\\coronavirus.csv",encoding = "ISO-8859-1")
df

df=df.drop([0,1,2,3,4,5,6,7,223,224,225,226,227,228,229,230])
df = df.drop(columns=['#'])

