import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = ".\df_real_and_predicted_pop.csv"
df = pd.read_csv(file, delimiter=',')

plt.plot(df['Year'][:41], df['Density'][:41])
plt.title('Population density over time prediction')
plt.xlabel("Year")
plt.ylabel("Density\n[person/sq km]")
plt.show()
