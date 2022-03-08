## API Documentation

### Following APIs have been used in the project:
- Google Maps API (Distance Matrix and Geocoding)
- Google Oauth API
- Openweathermap API  
  
  
### 1) Google Maps APIs  
<br>

#### API relevance
i) Distance Matrix API (from Google Maps): This API is used to access travel distance (in km) and time (in mins) for a matrix of origins and destinations.  
Documentation: [Overview|Distance Matrix API|Google Developers](https://developers.google.com/maps/documentation/distance-matrix/overview)

ii) Geocoding API (from Google Maps): This API is used to convert addresses (source and destination) into geographic coordinates (latitude and longitude)  
Documentation: [Overview|Geocoding API|Google Developers](https://developers.google.com/maps/documentation/geocoding/overview?hl=en_US)

#### API usage
Making the Distance Matrix and Geocoding API call: Required Parameters: Source address/Destination address and API key

#### Key generation steps
1) Create an account in Google Cloud Platform [Google Cloud Console](https://console.cloud.google.com/home/dashboard?project=rock-skyline-342820)  
2) Go to the Google Maps Platform > Credentials page.  
3) On the Credentials page, click Create credentials > API key.  
4) Go to APIs & Services and ensure the Distance Matrix API and Geocoding API are enabled for future use.  

### 2) Google Oauth API key   
<br>

#### API relevance
Google APIs use the OAuth 2.0 protocol for authentication and authorization. Google supports common OAuth 2.0 scenarios such as those for web server, client-side, installed, and limited-input device applications.  
Documentation: [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2)

#### API usage
Pass the client ID, secret and access token obtained from google and add it to your application configuration. Call the relevant APIs.

#### Key generation steps 
1) Obtain OAuth 2.0 credentials from the Google API Console.  
2) Obtain an access token from the Google Authorization Server.  
3) Examine scopes of access granted by the user.  
4) Send the access token to an API.  
<br>

If the above keys are generated successfully, following is the screenshot from the Google Cloud console.
![image_api1](./screenshots/image_api1.png)

<br>

### 3) Weather API (from OpenWeatherMap):   
<br>

#### API Relevance
This API is used to access current weather (clouds, destination, humidity, pressure, and wind) data for any location.   
Documentation: Current weather data - [OpenWeatherMap](https://openweathermap.org/current)  

#### API Usage
Required Parameters: Latitude, longitude, and API key
Python Request URL : https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)  

#### Key generation steps
1) Create a API key in OpenWeatherMaps once you sign up [OpenWeathermap signup](https://home.openweathermap.org/users/sign_up)  
2) Save the API key sent over to your signup email address.  

If the above keys are generated successfully, following is the screenshot from the OpenWeatherMap console.
![image_api2](./screenshots/image_api2.png)  
 
 <br>
 
**Note:** For generating the keys for Uber and Lyft APIs, the developers of the project are in talks with the engineers at these organizations to get the required access. This document will be updated once the server access tokens are granted.

