import joblib

from growthdata import xgb_clf
from envdata import xgb_reg
from aigrowth import rf

growth_model =  joblib.dump(xgb_clf,"growth_model.pkl")
production_model = joblib.dump(xgb_reg,"production_model.pkl")
grow_model = joblib.dump(rf,"grow_model.pkl")

def run_model(df):
    g = growth_model.predict(df)
    p = production_model.predict(df)
    j = grow_model.predict(df)
    return g, p, j
