import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = ".\df_real_and_predicted_pop.csv"
df = pd.read_csv(file, delimiter=',')

plt.plot(df['Year'], df['Population']/1000000000000, "g")
plt.xlabel("Year")
plt.ylabel("Population\n[trillions of people]")
plt.title('Population over time')
plt.show()
# Population change from 2000 to 2088
plt.plot(df['Year'][22:41], df['Population'][22:41]/1000000000, 'maroon')
plt.title('Population over time in XXI century')
plt.xlabel("Year")
plt.ylabel("Population\n[billions of people]")
plt.show()
