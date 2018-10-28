import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = ".\df_predicted_pop.csv"
df = pd.read_csv(file, delimiter=',')

plt.plot(df['Year'], df['Population']/1000000000000, "g")
plt.title('Population over time')
plt.xlabel("Year")
plt.ylabel("Population\n[trillions of people]")
plt.show()
