from surge_model_training import SurgePriceModel
from dynamic_pricing_model_training import PricePredictModel

surge_object = SurgePriceModel()
# surge_object.train_surge_classifier()

dynamic_price_object = PricePredictModel()
# dynamic_price_object.uber_train_test()
# dynamic_price_object.lyft_train_test()
