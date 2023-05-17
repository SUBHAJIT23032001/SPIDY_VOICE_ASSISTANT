from ast import Break
import datetime
import ctypes
from logging import shutdown
import os
from tracemalloc import start
from matplotlib.font_manager import ttfFontProperty
import pywhatkit
import webbrowser as web
from winsound import *
from pathlib import Path
from Listen import takeCommand
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import requests
import smtplib
from bs4 import BeautifulSoup
from Details import password,emailid,emailids_name
from say import speak
import time


                     

                
  

#Non input Functions:
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(time)

def Date():
    date = datetime.date.today()
    speak(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(day)

def ShutDown():
    speak("Tell me after how many hour or minute or seconds you want to shutdown the computer")
    T = takeCommand()
    t = str(T)
    try:
        if "hours" or "hour" in t:
            t = t.replace("after ","").replace(" hours","").replace("hour","").replace("shutdown","").replace("the","").replace("computer","")
            hour = int(t)*3600
            os.system("shutdown /s /t "+str(hour))
            speak("ok sir windows will shutdown after"+str(hour)+"hours")
        elif "minutes" or "minute" in t:
            t = t.replace("after ","").replace(" minutes","").replace("minute","").replace("shutdown","").replace("the","").replace("computer","")
            minute = int(t)*60
            os.system("shutdown /s /t "+str(minute))
            speak("ok sir windows will shutdown after"+str(minute)+"minutes")
        elif "seconds" or "second" in t:
            t = t.replace("after ","").replace(" seconds","").replace("second","").replace("shutdown","").replace("the","").replace("computer","")
            os.system("shutdown /s /t "+t)
            speak("ok sir windows will shutdown after"+t+"seconds")
    
    except Exception as e:
        os.system("shutdown /s /t 5")
        speak("windows will shutdown after 9 to 10 seconds")

def Restart():
    speak("Tell me after how many hour or minute or seconds you want to restart the computer")
    T = takeCommand()
    t = str(T)
    try:
        if "hours" or "hour" in t:
            t = t.replace("after ","").replace(" hours","").replace("hour","").replace("restart","").replace("the","").replace("computer","")
            hour = int(t)*3600
            os.system("shutdown /r /t "+str(hour))
            speak("ok sir windows will restart after"+str(hour)+"hours")
        elif "minutes" or "minute" in t:
            t = t.replace("after ","").replace(" minutes","").replace("minute","").replace("restart","").replace("the","").replace("computer","")
            minute = int(t)*60
            os.system("shutdown /r /t "+str(minute))
            speak("ok sir windows will restart after"+str(minute)+"minutes")
        elif "seconds" or "second" in t:
            t = t.replace("after ","").replace(" seconds","").replace("second","").replace("restart","").replace("the","").replace("computer","")
            os.system("shutdown /r /t "+t)
            speak("ok sir windows will restart after"+t+"seconds")
    except Exception as e:
        speak("Ok sir, Windows will restart in 9 to 10 seconds")
        os.system("shutdown /r /t 5")

def countdown(t):
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Times Up!')
        speak(" Your timer is over now")
        speak(" see you again")
        speak(" Bye bye")
#Input Functions:
def WhatsappMsg(name,message):

    startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=137, y=114)
    sleep(2)
    write(name)
    sleep(8)
    click(x=168, y=225)
    sleep(0.5)
    click(x=733,y=1006)
    sleep(1)
    write(message)
    press('enter')

def alarm(tt):

        
        Time = tt
        
        Time = Time.upper()
        altime = str(datetime.datetime.now().strptime(Time,"%I:%M %p"))
        
        altime = altime[11:-3]
        
        Hour_real = altime[:2]
        Hour_real = int(Hour_real)
        Min_real = altime[3:5]
        Min_real = int(Min_real)

        speak(f"Done, alarm is set for{Time}")
        S = False

        while True:
            if Hour_real==datetime.datetime.now().hour:
                if Min_real==datetime.datetime.now().minute:
                    PlaySound("mixkit-alarm-clock-beep-988.wav",SND_FILENAME)
                elif Min_real < datetime.datetime.now().minute:
                    S = True
            
            if S == True: 
                break

def SendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()#connect server
    server.starttls()
    server.login(emailid,password)
    server.sendmail(emailid,to,content)
    server.close()
    speak("email has been sent succesfully")




def NonInputExe(query):

    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "open WhatsApp" in query:
        startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif "shutdown" in query:
        ShutDown()
    elif "restart" in query:
        Restart()
    elif "lockscreen" in query:
        speak("ok sir")
        ctypes.windll.user32.LockWorkStation()

    


def InputExe(tag,query):
    
    if "wikipedia" in tag:
        try:

            name = str(query).replace("wikipedia","").replace("who is","").replace("what is","").replace("about","")
            import wikipedia
            result = wikipedia.summary(name, sentences=1)
            speak(result)
        
        except Exception as e:
            speak("sorry sir,I am not able to find this")
    
    elif "google" in tag:
        query = str(query).replace("google","").replace("search","").replace("google search","")
        
        pywhatkit.search(query) 

    elif "youtube" in tag:
         query = str(query).replace("youtube","").replace("yt","")
         r =  "https://www.youtube.com/results?search_query=" + query
        
         web.open(r)
         speak("This is what I found for you")
         speak("This may also help you boss")
         pywhatkit.playonyt(query)

    elif "maps" in tag:
        query = str(query).replace("google maps","").replace("maps","").replace("map","").replace("Search in google maps","").replace("in google maps","").replace("google","")
        url_place = "https://www.google.com/maps/place/" + query
        

        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(query, addressdetails = True)
        target_latlong = location.latitude , location.longitude
        location = location.raw['address']
        
        target = {'city': location.get('city',''),
                    'state': location.get('state',''),
                    'country' : location.get('country','')}

        current_location = geocoder.ip('me')
        current_latlong = current_location.latlng

        distance = str(great_circle(current_latlong,target_latlong))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)

        web.open(url=url_place)

        speak(target)
        speak(f"boss, {query} is {distance} Kilometre away from you")

    elif "whatsappmsg" in tag:
        query = str(query).replace("WhatsApp message","").replace("send","").replace("to","").replace("whatsapp","").replace("message","").replace("open","").replace("Open","")
        
        speak(f"Whats the message for {query}")
        Msg = takeCommand()
        WhatsappMsg(query,Msg)

    elif "open WhatsApp" in tag:
        startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    elif "temperature" in tag:

        query = str(query)
        url = f"https://www.google.com/search?q={query}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {query} is {temp}")
        
    elif "alarm" in tag:
        query = query.replace("set alarm at ","").replace(".","").replace("please set an alarm at ","")
        alarm(query)

    elif "email" in tag:
        try:
            query = query.replace("send email to ","").replace("send an email to ","")
            toemail = emailids_name[query]
            speak("What should I sent sir")
            C = takeCommand()
            SendEmail(toemail,C)
        except Exception as e:
            print(e)
            speak("Sorry email has not been sent due to some error")
    
    elif "countdown" in tag:
    
        try:
        
            if "hour" in query or "hours" in query:
                query = query.replace("set countdown for ", "").replace(".", "").replace("please set a countdown for ", "").replace("hour","").replace("hours","").replace("s","").replace("-","")
                sec = (int(query) * 60) * 60
                print("Timer is set for " + str(query) + " hour")
                speak("Timer is set for " + str(query) + " hour")
                countdown(sec)

            if "second" in query or "seconds" in query:
                query = query.replace("set countdown for ", "").replace(".", "").replace("please set a countdown for ", "").replace("second","").replace("seconds","").replace("s","").replace("-","")
                print("Timer is set for " + str(query) + " seconds")
                speak("Timer is set for " + str(query) + " seconds")
                countdown(int(query))

            if "minute" in query or "minutes" in query:
                query = query.replace("set countdown for ", "").replace(".", "").replace("please set a countdown for ", "").replace("minute","").replace("s","").replace("-","")
                sec = int(query)*60
                print("Timer is set for " + str(query) + " minutes")
                speak("Timer is set for " + str(query) + " minutes")
                countdown(sec)


            else:
                query = query.replace("set countdown for ", "").replace(".", "").replace("please set a countdown for ", "")
                print("Timer is set for " + str(query) + " seconds")
                speak("Timer is set for " + str(query) + " seconds")
                countdown(int(query))

        except Exception as e:
            print(e)
            speak("bhag bokachoda")



                    

        



       