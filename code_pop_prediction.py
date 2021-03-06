import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
plt.style.use('ggplot')

# PREPARING DATA
file = "df_pop.csv"  # downloaded from data.worldbank.org, cleaned in excel
df = pd.read_csv(file, delimiter=',')

land_area = 135 * 1_000_000  # 135 million sq km
max_density = 200_000  # 200 000 people per sq km
max_pop = land_area * max_density  # 27 * 10^12 = 27 trillion

df['Max_pop%'] = round(df['Population'] / max_pop * 100, 4)
df['Density'] = df['Population'] / land_area
df = df[['Year', 'Population', 'Max_pop%', 'Density']]
df = df[13:]
""" cutting off first 13 rows from dataset gives us
the best prediction accuracy score """

# Predicting Population amount depending on Year
X = np.array(df['Year']).reshape(-1, 1)
y = np.array(df['Population'])
forecast_out = 10  # amount of values to predict
X_train = X[:-forecast_out]
X_test = X[-forecast_out:]
y_train = y[:-forecast_out]
y_test = y[-forecast_out:]
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# Counting standard error
model = sm.OLS(y_pred, y_test).fit()
# print(f'Standard error: {model.bse})


# Plotting comparison of real and predicted population values
def plot_real_and_predicted_pop():
    plt.plot(X_test, y_test/1000000000,  color='r', label="Test values")
    plt.plot(X_test, y_pred/1000000000, color='b', label="Predicted values")
    plt.xlabel("Year")
    plt.ylabel("Population\n[billions of people]")
    plt.xticks(np.arange(2008, 2018, 1))
    plt.title("Test values vs predicted values")
    plt.text(2008, 7.5, ("Accuracy/variance score: "
             f"{round(r2_score(y_test, y_pred), 4)}"),
             bbox=dict(facecolor='red', alpha=0.2))
    plt.legend(loc="lower right")
    plt.savefig('plot_real_and_predicted_pop.png')
    plt.show()
plot_real_and_predicted_pop()

# Creating new Dataframe that will include future predictions
list = [0.05, 0.5, 1, 2, 5, 10, 25, 50, 75, 100]
a = np.empty((len(list), 1))
a[:] = np.nan
new_data = pd.DataFrame(a, columns=['Year'])
new_data['Max_pop%'] = list
new_data['Population'] = round(new_data['Max_pop%'] * max_pop / 100, 0)
new_data['Density'] = round(new_data['Population'] / land_area)
new_data['Density'] = new_data['Density'].astype(np.int64)
new_data = new_data[['Year', 'Population', 'Max_pop%', 'Density']]

# Predicting Year depending on Maximum Population Percentage
X_train = np.array(df['Max_pop%']).reshape(-1, 1)
y_train = df['Year']
X_pred = np.array(new_data['Max_pop%']).reshape(-1, 1)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_pred)
new_data['Year'] = np.round(y_pred, 0).astype(np.int64)

# Concatenating old and predicted DataFrames
f = pd.concat([df, new_data], ignore_index=True)
f['Density'] = np.round(f['Density'], 1)

# new_data.to_csv(".\df_predicted_pop.csv")
# f.to_csv(".\df_real_and_predicted_pop.csv")
