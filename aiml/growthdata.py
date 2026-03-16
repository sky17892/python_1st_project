from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from aigrowthdata import X_train, y_train, X_test, y_test

xgb_clf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

xgb_clf.fit(X_train, y_train)

pred = xgb_clf.predict(X_test)

print("RandomForest 정확도:", accuracy_score(y_test, pred))