import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "temperature":[25,26,27,28,24],
    "humidity":[60,65,70,55,68],
    "co2":[800,820,780,900,850],
    "light":[12000,13000,11000,15000,14000],
    "growth_stage":[0,1,1,2,0]
})
features = ['temperature','humidity','co2','light']
target = 'growth_stage'

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42
)

print("X_train")
print(X_train)

print("\nX_test")
print(X_test)