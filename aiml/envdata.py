from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

from aienvdata import X_train, y_train, X_test, y_test

xgb_reg = RandomForestRegressor(
    n_estimators=500,
    random_state=42
)

xgb_reg.fit(X_train, y_train)

pred = xgb_reg.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("🔥 RMSE:", rmse)
print("RandomForest regressor 정확도:", r2)

print("\n실제 vs 예측")
for real, p in list(zip(y_test[:10], pred[:10])):
    print(f"실제: {real:.2f} / 예측: {p:.2f}")