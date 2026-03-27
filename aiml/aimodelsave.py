import joblib

from growthdata import xgb_clf
from envdata import xgb_reg

growth_model =  joblib.dump(xgb_clf,"growth_model.pkl")
production_model = joblib.dump(xgb_reg,"production_model.pkl")

def run_model(df):
    g = growth_model.predict(df)
    p = production_model.predict(df)
    return g, p
