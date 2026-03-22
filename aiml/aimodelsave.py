import joblib

from growthdata import xgb_clf
from envdata import xgb_reg

joblib.dump(xgb_clf,"growth_model.pkl")
joblib.dump(xgb_reg,"production_model.pkl")