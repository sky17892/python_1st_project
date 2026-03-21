import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(112)
rows = 102

data = pd.DataFrame({
    "cultivation": np.random.randint(20, 30, rows),
    "production": np.random.randint(55, 65, rows),
    "growth": np.random.randint(780, 1000, rows),
    "environment": np.random.randint(8000, 18000, rows),
    "growth_stage": np.random.randint(0, 3, rows)
})

def make_target(row):
    score = 0

    if row['cultivation'] > 27:
        score += 1
    if row['production'] > 70:
        score += 1
    if row['growth'] > 850:
        score += 1
    if row['environment'] > 13000:
        score += 1

    if score <= 2:
        return 0
    elif score == 3:
        return 1
    else:
        return 2


data['growth_stage'] = data.apply(make_target, axis=1)

features = ['cultivation','production','growth','environment']
target = 'growth_stage'

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=112
)

print("X_train")
print(X_train)

print("\nX_test")
print(X_test)