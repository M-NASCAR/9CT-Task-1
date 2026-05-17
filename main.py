import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_module import (
                         display_df_preview,
                         clear_terminal,
                         search_df,
                         display_visualisation

                         )



df = pd.read_csv("domain_properties.csv", on_bad_lines='skip')
pd.set_option('display.float_format', '{:,.2f}'.format)
pd.set_option('display.max_rows', None)



#df['median_price'] = ['median_price']
#print(df)
suburb_df = df.groupby('suburb')['price'].median().reset_index()
suburb_df.columns = ['suburb', 'median_price']
suburb_df['km_from_cbd'] = suburb_df['suburb'].map(df.groupby('suburb')['km_from_cbd'].first())


def main_menu():  #Function for the main menu
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. Preview dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Exit")
    

        main_choice = input("Select an option (1-4): ").strip()

        if main_choice == '1':
            clear_terminal()
            display_df_preview()
        elif main_choice == '2':
            display_visualisation()
           


        elif main_choice == '3':
            clear_terminal()
            search_df()
        elif main_choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()

