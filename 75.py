import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
df.plot.scatter(x='x',y='y')
plt.show()