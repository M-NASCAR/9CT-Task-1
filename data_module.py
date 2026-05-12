import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("domain_properties.csv")

datetypes = pd.DatetimeIndex(df["date_sold"])
df["Year"] = datetypes.year


def display_df_preview():  #Function to Preview the Dataset
    print(df)
display_df_preview

suburb_df = df.groupby('suburb')['price'].median().reset_index()
suburb_df.columns = ['suburb', 'median_price']
suburb_df = suburb_df.sort_values('median_price', ascending=False)
print(suburb_df)


suburb_df.plot(
    kind="bar",
    x="suburb",
    y="median_price",
)



















'''
df.plot(kind="bar",
          x="num_parking",
          y="price",
          alpha=0.5
          )
'''


plt.show()


