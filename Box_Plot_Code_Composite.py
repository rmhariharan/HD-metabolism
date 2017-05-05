import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale = 1.0)
sns.set_style("white", {"axes.linewidth": "0","axes.labelcolor":"0.1"})
sns.despine()
# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), sharex=True, sharey = True)




mydata = pd.read_csv("C:/Users/rharihar/Desktop/CHDI_PROJECT/HD_metabolism_paper/Robustness_Combined_Seaborn.csv",index_col = None)

#mydata = data

    ha = ['right', 'center', 'left']
sns.boxplot(data = mydata, x = "Age_Q_length",y = "Number_Striatum", palette = "Blues", width = 0.7, ax = ax1)
ax1.set_xlabel("Striatum")
ax1.set_ylabel(" ")
sns.boxplot(data = mydata, x = "Age_Q_length",y = "Number_Cortex", palette = "Blues", width = 0.7, ax = ax2)
ax2.set_xlabel("Cortex")
ax2.set_ylabel("Number of Pathways")
sns.boxplot(data = mydata, x = "Age_Q_length",y = "Number_Liver", palette = "Blues", width = 0.7, ax = ax3)
ax3.set_xlabel("Liver")
ax3.set_ylabel(" ")

#sns.swarmplot(data = mydata, x = "Age & Q length",y = "Number of Pathways", color = "0.25")
sns.plt.xticks(rotation = 90, ha = ha[1])
#sns.plt.savefig("C:/Users/rharihar/Desktop/testing_box.png",format = 'png',dpi = 300,bbox_inches = 'tight')
sns.plt.show()
