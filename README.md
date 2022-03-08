![logo file](/cab-dynamic-pricing/templates/logo.jpg)

## Easy Cabs
Easy Cabs helps you in getting the dynamic pricing of an Uber and Lyft. Input your source and destination and Easy Cabs will take into account your lattitude, longitufe, weather forecast and predict the surge pricing for your rides on both the apps. The end user can then make a decision on which cab would be the best for them in terms of cost and ETA.

## Background


## Data
[Data Set](https://www.kaggle.com/ravi72munde/uber-lyft-cab-prices). 

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
  - surge_multiplier : 4 values mentioned. 
  - temp : temperature in Fahrenheit.
  - time_stamp : start of the cab journey in epoch units.
  - wind : wind speed in miles per hour.

## Project Distribution

```
cab-dynamic-pricing/
  |- README.md
  |- cab-dynamic-pricing/
    |- __init__.py
    |- configuration_files/
      |- __pycache__/
        |- software_configuration.cpython-39.pyc
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
    |- test/
      |-
      |-
      |-
    |- utils/
      |- geospatial_information.py
      |- lyft.py
      |- uber.py
      |- user.py
      |- utils.py
      |- weather_information.py
    | - app.py
  |- data/
      |- cab_rides.csv.zip
      |- weather.csv
  |- example
      |-
      |-
  |- .coveragerc
  |- .gitignore
  |- Experimentation.ipynb
  |- LICENSE
  |- requirements.txt
  |- setup.py
```
## Installation


## Usage

To see how to use the package to get instance recommendation, 
refer to the [example notebook](examples/examples.ipynb)

---
## The Output
Below is an image of how the output of our recommendation looks like.
![sample_reccommendation](./docs/sample-recommendation.PNG)
