import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("domain_properties.csv")
pd.set_option('display.float_format', '{:.2f}'.format)


df.groupby('suburb')
#df['median_price'] = ['median_price']
print(df)

#suburb_df["km_from_cbd"] = df["km_from_cbd"]

#print(suburb_df)
#df["Mean_price"] = df["suburb"].map(suburb_df)

def display_df_preview():  #Function to Preview the Dataset
    print("1. Preview Dataset")
    print("2.Search for details on a specific suburb:")
    print("3.Exit")
    choice = input("Select an option (1-3): ").strip()
    while choice != "3":
        if choice == "1":
            print(df)
           

        elif choice == "2":
            userinput = input("Enter the suburb you wish to know the mean price of: ").strip().title()
            result = df[df['suburb'] == userinput]
            if result.empty:
                print("Suburb Not found, Try again.")
            else:
                print(result)
display_df_preview()



'''
suburb_df.plot(
 kind="bar",
 x="suburb",
 y="mean_price",
)
'''







#plt.show()


