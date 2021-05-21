import numpy as np
import pandas as pd
from matplotlib import pylpot as plt

pie = np.array(([425, 125], [62,8]))
pie_df = pd.DataFrame(pie, index=['possible','virtuel'], columns=['ADJ','NOUN']).T
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
pie_df['possible'].plot.pie(autopct='%1.0f%%')
plt.subplot(1,2,2)
pie_df['virtuel'].plot.pie(autopct='%1.0f%%')
