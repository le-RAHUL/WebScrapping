import requests, json

api_key = "05d6694161fcb0b6acea7621170265c5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input()

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

# Storing the json values in a variable
x = response.json()

#If the return code is not 404, process the data else throw error to user
if x["cod"] != "404":

    y = x["main"]

    temperature = y["temp"]
    pressure = y["pressure"]
    humidiy = y["humidity"]
    min_temp = y['temp_min']
    max_temp = y['temp_max']

    f = open("weather_data.doc",'w',encoding = 'utf-8')
    f.write(city_name)
    f.write("\n")

    f.write("pressure: "+str(pressure) +'\t'+"Humidity: " + str(humidiy) +'\t' +"Temperature: " +str(temperature) +'\t' + "min_temp: "+str(min_temp) +'\t' +"max_temp: "+ str(max_temp))
    f.close()
    print("Write Sucessful")
else:
    print(" City Not Found ")

    