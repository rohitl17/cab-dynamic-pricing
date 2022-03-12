## Functional Specifications 


### Background  
Uber and Lyft are the top companies working in the cabs domain. Users have to put in the location in each of the apps to get the optimal cost. Our ML-based solution incorporating surge overcomes this by being a one-stop solution for comparing prices for different types of cabs. The surge calculation tries to replicate Uber's microservice for pricing and surging calculation by taking into account the rush hours, weather changes and location. The dynamic pricing ML model uses the surge, distance, cab type source and destination location features to calculate the final price. Our goal is to suggest the user an appropriate cab type from Uber and Lyft as per their budget constraints and convenience.


### User profile  
- General Populace: People who want to compare Uber and Lyft cabs and book them at a optimal cost.


### Data sources
- [Data Set](https://www.kaggle.com/ravi72munde/uber-lyft-cab-prices) from Kaggle which has over 693000 records of data for weather and cab-rides. 


### Use cases   

<ol>
<li>Choosing a cab from Uber and Lyft of similar types as per cost
  <ol>
    <li>USER: Enters source and destination.</li>
    <li>USER: Provides similar cab types for uber and lyft.</li>
    <li>PROGRAM: Runs the model for surge prediction.</li>
    <li>PROGRAM: Runs the model for dynamic price calculation using the surge prediction model output.</li>
    <li>OUTPUT: Outputs the price for uber, lyft respective cab types and ETA and distance between the source and destination.</li>
  </ol>
</li> 
  
  
<li>Choosing a cab from Uber and Lyft of different types as per cost and convenience 
  <ol>
    <li>USER: Enters source and destination.</li>
    <li>USER: Provides luxury or different cab types for uber and lyft.</li>
    <li>PROGRAM: Runs the model for surge prediction.</li>
    <li>PROGRAM: Runs the model for dynamic price calculation using the surge prediction model output</li>
    <li>OUTPUT: Outcomes the price for uber, lyft respective cab types and ETA and distance between the source and destination.</li>
  </ol>
</li>
</ol>
