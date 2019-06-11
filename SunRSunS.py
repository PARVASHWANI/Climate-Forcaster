#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests, json
#OPEN WEATHER MAP API
api_keyW = "Enter Your Own API From"
base_urlW = "http://api.openweathermap.org/data/2.5/weather?units=metric&cnt=7&lang=en&"
city_name = input("Enter City Name: ")
complete_urlw = base_urlW+ "appid=" + api_keyW + "&q=" + city_name


# In[34]:


complete_urlw


# In[35]:


responsew = requests.get(complete_urlw)


# In[36]:


y = responsew.json()


# In[37]:


z = y['main']
cur_temp = z["temp"]
cur_pres = z["pressure"]
cur_humi = z["humidity"]
min_temp = z["temp_min"]
max_temp = z["temp_max"]
visibili = ["visibility"]
w = y["wind"]
wind_speed = w["speed"]
wind_deg = w["deg"]


# In[38]:


longi = y['coord']['lon']
latti = y['coord']['lat']


# In[39]:


###create base_url(isme paremeter nahi hote hai)
#phir jitne bhee parameter chahie utne paremeter bana lijye
base_url = "https://api.sunrise-sunset.org/json"
latitude = str(latti)
longitude = str(longi)
complete_url = base_url + '?lat=' + latitude + '&lng=' + longitude


# In[40]:


#https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
complete_url


# In[41]:


#Response banana hai
#respose module me 'get' naam ka methord hota hai jista argument complete URL hota
response = requests.get(complete_url)


# In[42]:


x = response.json()


# In[43]:


sunset = x['results']['sunset']


# In[44]:


sunrise = x['results']['sunrise']


# In[45]:

print(" Current Temprature(In Celsius  unit) = " + str(cur_temp) +
      "\n Atmospheric Pressure (in hPa unit) = " + str(cur_pres) +
      "\n Humidity (in percentage) = " + str(cur_humi) +
      "\n Minimum Temprature = " + str(min_temp) +
      "\n Maximum Temprature = " + str(max_temp) +
      "\n Wind Speed =" + str(wind_speed) +
      "\n Degree = " + str(wind_deg) +
      "\n Sunrise (in UTC) = " + str(sunrise) +
      "\n Sunset (in UTC) = " + str(sunset))
