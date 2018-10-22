import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = ".\df_real_and_predicted_pop.csv"
df = pd.read_csv(file, delimiter=',')

plt.plot(df['Year'], df['Population'], "g")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
# Population change from 2000 to 2088
plt.plot(df['Year'][22:41], df['Population'][22:41], 'r')
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
