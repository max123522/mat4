# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:00:05 2021

@author: micha
"""
import requests
import re

def list_address():
    file=open("dests.txt",encoding="utf8")
    list_dest=list()
    for line in file:
        list_dest.append(line.strip())
    for i in range(len(list_dest)):
        distance(list_dest[i])    
    print(dictAll)
   
    city1='' 
    city2=''
    city3=''
    distance_city1=0 
    distance_city2=0
    distance_city3=0
    distancesArray = []
    DeleteKm = re.compile(r"([^km]+)") 
    for j in distancecity:
        HaveKm = DeleteKm.search(j)
        if HaveKm:
            distancesArray.append(j[HaveKm.span()[0]:HaveKm.span()[1]].replace(' ','').replace(',','')) 
    distancesArray = [float(j) for j in distancesArray] 
    for j in range(len(distancesArray)):
        if distancesArray[j]>distance_city1:
            distance_city3=distance_city2
            distance_city2=distance_city1
            distance_city1=distancesArray[j]
            city3=city2
            city2=city1
            city1=list_dest[j] 
        elif distancesArray[j]>distance_city2:
            distance_city3=distance_city2
            distance_city2=distancesArray[j]
            city3=city2
            city2=list_dest[j]
        elif distancesArray[j]>distance_city3:
            distance_city3=distancesArray[j]
            city3=list_dest[j]

    print('\n' ,"The 3 furthest cities from Tel-aviv are:", 
          '\n','1)', city1.strip(),' = ', distance_city1, 'km'
          '\n','2)', city2.strip(),' = ', distance_city2, 'km'
          '\n','3)', city3.strip(),' = ', distance_city3, 'km')
    
    
        
def distance(destination):
    Api_Key="מופיע בקובץ שהוגש במודל"
    Address="תל אביב"
    url_dest="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(Address,destination,Api_Key)
    response_destination=requests.get(url_dest)
    # print(response_destination.status_code)
    response_destination=requests.get(url_dest).json()
    try:
        distance = response_destination['rows'][0]['elements'][0]['distance']['text']
        duration= response_destination['rows'][0]['elements'][0]['duration']['value']
    except:
        print("the distancematrix doesnt work beacose the" + " "+ destination + " " +  "is not exsist")
    
    url_gecode="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(destination,Api_Key)
    response_gecode=requests.get(url_gecode).json()
    try:
        lati = response_gecode['results'][0]['geometry']['location']['lat']
        long = response_gecode['results'][0]['geometry']['location']['lng']
        lati ='lat:'+ str(lati)
        long ='lng:'+ str(long)
        distancecity.append(distance)
        if((duration/3600)<1):
            duration=duration/60
            duration=str(duration) +""+ 'min'
        else:
            hours=int(duration/3600)
            minutes=round(((duration%3600)/3600)*60,2)
            duration=str(hours)+' hours '+ str(minutes)+ ' min '
        tuppledetail=(distance,duration)+(lati,long)
        dictAll[destination]=tuppledetail
    except:
        print("the gecode doesnt work beacose the " + destination + " " +  "is not exsist")


    

dictAll=dict()
distancecity = list()
list_address()