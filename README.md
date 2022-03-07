## cab-dynamic-pricing

## Project Distribution


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
  |- .coveragerc
  |- .gitignore
  |- Experimentation.ipynb
  |- LICENSE
  |- requirements.txt
  |- setup.py
