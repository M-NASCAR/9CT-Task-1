import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("domain_properties.csv", on_bad_lines='skip')
pd.set_option('display.float_format', '{:.2f}'.format)



#df['median_price'] = ['median_price']
#print(df)
suburb_df = df.groupby('suburb')['price'].median().reset_index()
suburb_df.columns = ['suburb', 'median_price']
suburb_df['km_from_cbd'] = suburb_df['suburb'].map(df.groupby('suburb')['km_from_cbd'].first())
    
#suburb_df["km_from_cbd"] = df["km_from_cbd"]

#print(suburb_df)
#df["Mean_price"] = df["suburb"].map(suburb_df

def clear_terminal(): #Clears the terminal and decides what operation to use based on the operating system
      os.system('cls' if os.name == 'nt' else 'clear') 



def preview_menu(): #Function for the Menu inside the data preview section
    print("1. Preview Dataset")
    print("2.Search for details on a specific suburb:")
    print("3.Exit")
    


def display_df_preview():
    while True:
        preview_menu() #Function to Preview the Dataset
        choice = int(input("Select an option (1-3): ").strip())
        if choice == 1:
            print(df)
            preview_menu()
            choice = int(input("Select an option (1-3): ").strip())
           

        elif choice == 2:
            userinput = input("Enter the suburb that you wish to know median house prices in: ").strip().title()
            result = suburb_df[suburb_df['suburb'] == userinput][['suburb', 'median_price','km_from_cbd']].drop_duplicates(subset='suburb')
            if result.empty:
                print("Suburb Not found, Try again.")
                print("2.Search for details on a specific suburb:")
                print("3.Exit")
                choice = int(input("Select an option (1-3): ").strip())

            else:
                print(result)
                print("2.Search for details on a specific suburb:")
                print("3.Exit")
                choice = int(input("Select an option (2-3): ").strip())



        elif choice == 3:
                clear_terminal()
                main_menu()
                break
        else:
                print("Not a valid option please try again")
         














'''
suburb_df.plot(
 kind="bar",
 x="suburb",
 y="mean_price",
)
'''







#plt.show()


