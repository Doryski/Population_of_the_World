import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = ".\predicted_pop.csv"
df = pd.read_csv(file, delimiter=',')
df = df[:4]

plt.plot(df['Year'], df['Population'])
plt.show()
