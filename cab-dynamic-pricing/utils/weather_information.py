import requests, json

def weather_information(latitude, longitude):
    api_key = ""
    latitude = "48.208176"
    longitude = "16.373819"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, api_key)
    response = requests.get(url)
    response_data = json.loads(response.text)
    
    weather_model_parameters_dict={}
    
    weather_model_parameters_dict['temp']=response_data['current']['temp']
    weather_model_parameters_dict['Clouds']=response_data['current']['clouds']
    weather_model_parameters_dict['pressure']=response_data['current']['pressure']
    weather_model_parameters_dict['rain']=response_data['current']['precipitation']
    weather_model_parameters_dict['humidity']=response_data['current']['humidity']
    weather_model_parameters_dict['wind']=response_data['current']['wind_speed']
    
    current_weather_df=pd.DataFrame.from_dict(weather_model_parameters_dict)
    
    return current_weather_df