import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

df = pd.read_csv('/media/prince/5A4E832F4E83034D/Visualization practice /Data/candy.csv')


plt.figure(figsize=(8,5))

plt.scatter(
    df['sugarpercent'],
    df['winpercent'],
    alpha=0.75,
    s=60,
    edgecolors='white',
    linewidth=0.5,
    c=df['winpercent'],          # color = popularity
    cmap='plasma'
)

plt.xlabel("Sugar Percent")
plt.ylabel("Win Percent")
plt.title("Sweetness vs Popularity")
plt.colorbar(label="Popularity (Win %)")
plt.grid(alpha=0.3)
plt.show()
