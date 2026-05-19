import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("domain_properties.csv", on_bad_lines='skip')
pd.set_option('display.float_format', '{:,.2f}'.format)
pd.set_option('display.max_rows', None)


suburb_df = df.groupby('suburb')['price'].median().reset_index()
suburb_df.columns = ['suburb', 'median_price']
suburb_df['km_from_cbd'] = suburb_df['suburb'].map(df.groupby('suburb')['km_from_cbd'].first())
    


def clear_terminal():
    print("\033[H\033[J", end="")
  
    


def display_df_preview():
    while True:
       
          print("1. Preview Dataset")
          print("2.Exit")
          choice = int(input("Select an option (1-2): ").strip())
          clear_terminal()

          if choice == 1:
              print(df.head(10).to_string(index=False))
          

          elif choice == 2:
                clear_terminal()
                break
          else:
                print("Not a valid option please try again")
         

def display_visualisation():
    
    plt.scatter(suburb_df["km_from_cbd"], suburb_df["median_price"],alpha=0.5,color='red')
    plt.xlabel("Distance from Sydney CBD (km)") 
    plt.ylabel("Median house price ($)")
    plt.title("Greater Sydney House Prices vs Distance from CBD")
    plt.ticklabel_format(style='plain')
        
    plt.tight_layout()  
    plt.show(block=False)
    
    input("Press Enter to return to the menu...")
    plt.close()
    clear_terminal()

    





def search_df():
     clear_terminal()
     while True:
        print("1. Search data for specific suburb details")
        print("2.Filter Search")
        print("3.Exit")
        search_choice = int(input("Enter an option 1-3:"))

       

        if search_choice == 1:

            userinput = input("Enter the suburb that you wish to know median house prices in: ").strip().title()
            result = suburb_df[suburb_df['suburb'] == userinput][['suburb', 'median_price','km_from_cbd']].drop_duplicates(subset='suburb')

            if result.empty:
                print("Suburb Not found, Try again.")
                clear_terminal()

            else:
                clear_terminal()
                print(result)

        elif search_choice == 2:
            clear_terminal()
            print("1. Filter by distance from CBD")
            print("2. Filter by median house price")
            print("3.Exit")
            filter_choice = int(input("Select an option(1-3):"))

            if filter_choice == 1:
                 filter = int(input("Filter within X kilometres"))
                 print(suburb_df[suburb_df['km_from_cbd'] <= filter])


            elif filter_choice == 2:
                clear_terminal()
                print("1.Search for results over $X")
                print("2.Search for results under $X")
                print("3.Exit")
                price_filter_choice = int(input("Select an option 1-3:"))


                if price_filter_choice == 1:
                    filter = int(input("Filter results over than $X, Enter X:"))
                    result = suburb_df[suburb_df['median_price'] >= filter]
                    if result.empty:
                        print("No Results found please try again.")
                    else:
                        print(result.to_string(index=False))
                elif price_filter_choice == 2:
                    filter = int(input("Filter results less than $X, Enter X:"))
                    result = suburb_df[suburb_df['median_price'] <= filter]
                    if result.empty:
                        print("No Results found please try again.")
                    else:
                        print(result.to_string(index=False))
                elif filter_choice == 3:
                    break
                else:
                    print("Not a valid option, please select an option 1-3")


            elif filter_choice == 3:
                break
            else:
                print("Not a valid Option please try again")
              
        elif search_choice == 3:
            clear_terminal()
            break
        else:
            clear_terminal()
            print("Not a valid option, please try again")



         



     



     
  










