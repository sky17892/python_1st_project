import joblib

from growthdata import xgb_clf

joblib.dump(xgb_clf,"growth_model.pkl")
#joblib.dump(xgb_reg,"production_model.pkl")