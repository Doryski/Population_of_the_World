import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
plt.style.use('ggplot')

### PREPARING DATA
file = ".\pop.csv" # downloaded from data.worldbank.org, cleaned in excel
df = pd.read_csv(file, delimiter=';')

land_area = 135 * 1000000 # 135 million sq km
max_density = 200000 # 200 000 people per sq km
max_pop = land_area * max_density # 27 * 10^12 = 27 trillion

df['Max_pop%'] = round(df['Population'] / max_pop * 100, 4)
df['Density'] = df['Population'] / land_area
df = df[['Year','Population','Max_pop%','Density']] # created dataframe
df = df[13:] # cutting off first 13 years from dataset gives us the best prediction accuracy score
### Predicting Population amount depending on Year
X = np.array(df['Year']).reshape(-1,1)
y = np.array(df['Population'])
forecast_out = 10
X_train = X[:-forecast_out]
X_test = X[-forecast_out:]
y_train = y[:-forecast_out]
y_test = y[-forecast_out:]
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print('Accuracy/variance score: %.2f' % r2_score(y_test, y_pred)) # 0.966
# Counting standard error
import statsmodels.api as sm
model = sm.OLS(y_pred, y_test).fit()
#print('Standard error:', model.bse) # [0.00061961]

# Plotting comparison of real and predicted population values
plt.plot(X_test, y_test,  color='r')
plt.plot(X_test, y_pred, color='b')
plt.show()
### Creating new Dataframe that will include future predictions
list = [0.05,0.5,1,2,5,10,25,50,75,100]
a = np.empty((len(list),1))
a[:] = np.nan
new_data = pd.DataFrame(a, columns=['Year'])
new_data['Max_pop%'] =  list
new_data['Population'] = round(new_data['Max_pop%'] * max_pop / 100, 0)
new_data['Density'] = round(new_data['Population'] / land_area).astype(np.int64)
new_data = new_data[['Year','Population','Max_pop%','Density']]

### Predicting Year depending on Maximum Population Percentage
X_train = np.array(df['Max_pop%']).reshape(-1,1)
y_train = df['Year']
X_pred = np.array(new_data['Max_pop%']).reshape(-1,1)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_pred)
new_data['Year'] = np.round(y_pred, 0).astype(np.int64)

### Concatenating old and predicted DataFrames
f = pd.concat([df, new_data], ignore_index=True)
f['Density'] = np.round(f['Density'],1)

# new_data.to_csv(".\predicted_pop.csv")
# f.to_csv(".\real_and_predicted_pop.csv")
