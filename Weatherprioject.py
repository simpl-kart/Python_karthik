import requests
api_key="893760528276fd4a9ccedf8d4e0ac256"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_id = input("Enter city id: ")
url = base_url + "id=" + city_id + "&APPID=" + api_key
response = requests.get(url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    temp_minimum = y["temp_min"]
    temp_maximum = y["temp_max"]
    z = x["weather"]
    a = x["sys"]
    weather_description = z[0]["description"]
    sunrise_det = a["sunrise"]
    sunset_det = a["sunset"]
    country_det = a["country"]
    city_det = x["name"]
    print(" Temperature (in kelvin unit)         = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hpa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage)           = " +
          str(current_humidiy) +
          "\n minimum temperature                = " +
          str(temp_minimum) +
          "\n maximum temperature                = " +
          str(temp_maximum) +
          "\n sunrise details                    = " +
          str(sunrise_det) +
          "\n sunset details                     = " +
          str(sunset_det) +
          "\n current city                       = " +
          str(city_det) +
          "\n description                        = " +
          str(weather_description))
else:
    print(" City id is unavailable")