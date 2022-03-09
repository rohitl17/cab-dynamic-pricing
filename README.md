[![Build Status](https://app.travis-ci.com/rohitl17/cab-dynamic-pricing.svg?branch=main)](https://app.travis-ci.com/rohitl17/cab-dynamic-pricing) [![Coverage Status](https://coveralls.io/repos/github/rohitl17/cab-dynamic-pricing/badge.svg?branch=main)](https://coveralls.io/github/rohitl17/cab-dynamic-pricing?branch=main) ![contributors](https://img.shields.io/github/contributors/rohitl17/cab-dynamic-pricing.svg) ![codesize](https://img.shields.io/github/languages/code-size/rohitl17/cab-dynamic-pricing.svg)

![logo file](/cab-dynamic-pricing/templates/logo.jpg)

## Easy Cabs
Easy Cabs helps you in getting the dynamic pricing of an Uber and Lyft. Input your source and destination and Easy Cabs will take into account your lattitude, longitufe, weather forecast and predict the surge pricing for your rides on both the apps. The end user can then make a decision on which cab would be the best for them in terms of cost and ETA.

## Background
A web application for calculating the dynamic price of Uber and Lyft cabs depending on various attributes. 
Machine learning models are built to calculate the surge multiplier and the price of the cab between two different locations across the city of Boston.
The user enters the source and destination along with the choice of cab for Uber and Lyft each and hit the "Calculate Price" button.  
The user will be prompted with the cost of price for the particular cab for Uber and Lyft in USD, along with the ETA in minutes and distance in miles.  

## Authors
- [Nayantara Mohan](https://github.com/nayantaramohan)  
- [Rohit Lokwani](https://github.com/rohitl17)  
- [Shubha Changappa Palachanda](https://github.com/shubha8196)

## Project Distribution

```
cab-dynamic-pricing/
  |- README.md
  |- cab-dynamic-pricing/
    |- __init__.py
    |- configuration_files/
      |- software_configuration_format.py
    |- database/
      |- users.csv
    |- feedback_app/
      |- training_testing_data/
        |- lyft_test_mlr.csv
        |- lyft_train_mlr.csv
        |- testing_surge_price_classifier_df.csv
        |- training_surge_price_classifier_df.csv
        |- uber_test_mlr.csv
        |- uber_train_mlr.csv
      |- dynamic_price_model_training.py
      |- surge_model_training.py
      |- train_models.py
    |- model_scripts/
      |- dynamic_pricing_regression_inference.py
      |- surge_classification_inference.py
    |- model_weights/
      |- lyft_mlr_model.sav
      |- surge_classification_rf_model.sav
      |- uber_mlr_model.sav
    |- templates/
      |- login_background.jpg
      |- login_index.html
      |- template_page2.html
    |- tests/
      |- test_app.py
      |- test_dynamic_pricing_model_training.py
      |- test_dynamic_pricing_regression_inference.py
      |- test_geospatial_information.py
      |- test_lyft.py
      |- test_software_configuration_format.py
      |- test_surge_classification_inference.py
      |- test_surge_price_model.py
      |- test_train_models.py
      |- test_uber.py
      |- test_user.py
      |- test_weather_information.py
    |- utils/
      |- geospatial_information.py
      |- lyft.py
      |- uber.py
      |- user.py
      |- utils.py
      |- weather_information.py
    | - app.py
  |- data/
      |- cab_rides.csv.zipe
      |- weather.csv
  |- documentation/
      |- api_documentation.md
      |- component_specification.md
      |- functional_specification.md
      |- screenshots/
  |- example
      |- example.md
      |- screenshots/
  |- .coveragerc
  |- .gitignore
  |- LICENSE
  |- requirements.txt
  |- setup.py
```
  
  
## Data
[Link to the Data Set](https://www.kaggle.com/ravi72munde/uber-lyft-cab-prices)   
Features extracted from the dataset: -
  - cab_type : Uber or Lyft.
  - clouds : presence or absence of clouds.
  - destination : name of the destination in words.
  - humidity : humidity in percentage.
  - location : location of the place where the weather is recorded.
  - pressure : atmospheric pressure in millibar.
  - price : price estimate for the ride in USD.
  - rain : rain in inches for the last hour.
  - name : type of the car specified, eg. X, XL.
  - source : name of the source in words.
  - surge_multiplier : 5 unique values mentioned. 
  - temp : temperature in Fahrenheit.
  - time_stamp : start of the cab journey in epoch units.
  - wind : wind speed in miles per hour.
  
## Installation

Installing the package using the pip command:
```bash
pip install cab-dynamic-pricing
```  
Install the dependencies from the requirements.txt file using the below:
```bash
python -m pip install -r requirements.txt
```
## Usage and Output

To see how to use the package to get the dynamic pricing of Uber and Lyft,   
refer to the [example file](./example/example.md)
