import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("energy.csv")
data = data[["Combustible Fuel Power", "Hydropower", "Solar Power"]]

X = data[["Combustible Fuel Power", "Hydropower"]]
y = data["Solar Power"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("***************")
print("Testing Results")
