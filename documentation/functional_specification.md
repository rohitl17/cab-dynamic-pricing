Functional Specifications Background. There are various companies working in the cab domain. Uber and Lyft being amongst the top of them. Users have to put in the location in each of the apps to get the optimal cost. Our ML-based solution incoroporating surge overcomes this by being one-stop solution for comparing prices for different types of cabs. The surge calulation tries to replicate Uber's microservice for surge calculation by taking into account the rush hours, weather changes and location. The dynamic pricing ML model uses the surge, distance and other features to calculate the final price. Our goal is to suggest the user an appropriate cab type from Uber and Lyft as per their budgets and constraints.

User profile. General Populace: People who want to compare and book cabs at optimal cost.

Data sources. Data from Kaggle which has data for weather and cab-rides information (Put link here)

Use cases. Choosing a cab from Uber and Lyft as per cost
USER: Enters source and destination USER: Provides similar cab types for uber and lyft PROGRAM: Runs the model for surge prediction PROGRAM: Runs the model for dynamic price calculation OUTPUT: Outcomes the price for uber, lyft respective cab types and ETA and distance between the source and destination.

Choosing a cab from Uber and Lyft as per cost
USER: Enters source and destination USER: Provides different cab types for uber and lyft PROGRAM: Runs the model for surge prediction PROGRAM: Runs the model for dynamic price calculation OUTPUT: Outcomes the price for uber, lyft respective cab types and ETA and distance between the source and destination.
