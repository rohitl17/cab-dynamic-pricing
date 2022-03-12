## Software Components  

### Component 1: (app)
Call the the Google Oauth API for authentication  
Input: User's Google email ID and password.  
If login is successful, take the user to the next page else reload the home page


### Component 2: (getCabPrice)
Input: Source, destination and type of cabs.  
The component then calls the following subcomponents to get the required values:  
1. Geospatial Data : Input: Source and Destination; Output: Latitude and Longitude, ETA and Distance. 
2. Weathermap API: Input: Source Latitude and Longitude; Output: Required weather parameters. 
3. Uber API: Input: source and destination; Output: dynamic Price and surge multiplier of the required cab <sup>*</sup>. 
4. Lyft API: Input: source and destination, Output: dynamic Price and surge multiplier of the required cab <sup>*</sup>


### Component 3: (surge_inference)
Input: Weather parameters obtained in getCabPrice Component 2. 
Run the classification model to calculate surge. 
Return: surge_price

### Component 4: (dynamic_price_inference)
Input: Surge, distance, source and destination geospatial information   
Runs the data manipulation and the regression model to calculate dynamic price for uber and lyft individually. 
Return (Price for Uber and Lyft selected cab prices)

### Component 5: (result_generator)
Input JSON for the output from previous steps to show the final user the report. 
Creates a JSON and shows the output on a blank page with logout option or back button to try other combinations. 
Output: Price , ETA and Distance estimates for the user

### Component 6: (feedback loop using cron job)
Input the dataframe with parameters obtained in Component 2, using price from Lyft and Uber API as their ground truth.  
A cron job can be configured by the developer to run and save the results everytime. The default configuration is running every friday night 11pm.  
Output: Retrained models for surge classification and dynamic pricing.

### Component 7 (database):
This component is under development now. The developers plan to store the basic user information for storing user context for future logins. This database will also store updated model results and entries for feedback application. It uses CSVs now.

### Components interaction
1. User visits the home page. Signs in using google email ID. The backend for this authentication is handled by the component 1. In case of successful login, the user is directed to the Component 2.  
2. For component 2, the user inputs the required source, destination and selects uber and lyft cab types from the dropdown. This then directs the context to the involved subcomponents to get the required information using the APIs.  
3. Once the information is available, the component 3 is called and calulates the surge using the ML model.  
4. The surge is sent to component 4 which calculates the dynamic price for the respective cab prices.  
5. Once the price is calculated, the final report is generated as a JSON and sent to the reporting frontend which shows the output.  
6. The component 6 is an independent component which interacts through the component 7 (database) with the other components. The components 1 and 2 store the user related and model specific information in the database. This information is used to retrain the models at specified intervals using a cron job. 

### The Output
The HTML file created by report_generator:
![image_api3](./screenshots/image_api3.png)

<br>
<sup>*</sup> Implementation in progress as the tokens were not available from the Uber or Lyft's developer platforms.
