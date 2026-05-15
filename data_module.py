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

def clear_terminal():
     os.system('cls')



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
                print(67)
                break
        else:
                print("Not a valid option please try again")
         







def main_menu():  #Function for the main menu
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. Preview dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Update a data entry")
        print("5. Save changes")
        print("6. Exit")

        main_choice = input("Select an option (1-6): ").strip()

        if main_choice == '1':
            clear_terminal()
            display_df_preview()
        elif main_choice == '2':
            display_visualisation()
        elif main_choice == '3':
            search_data()
        elif main_choice == '4':
            update_data_entry()
        elif main_choice == '5':
            save_changes()
            print("Changes saved.")
        elif main_choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()








'''
suburb_df.plot(
 kind="bar",
 x="suburb",
 y="mean_price",
)
'''







#plt.show()


