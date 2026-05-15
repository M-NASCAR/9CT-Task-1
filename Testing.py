import pandas as pd

df = pd.read_csv("domain_properties.csv", on_bad_lines='skip')
pd.set_option('display.float_format', '{:.2f}'.format)

def display_df_preview(): 
    preview_menu() #Function to Preview the Dataset
    choice = int(input("Select an option (1-3): ").strip())
    while choice != 3:
        if choice == 1:
            print(df)
            preview_menu()
            choice = int(input("Select an option (1-3): ").strip())
           

        elif choice == 2:
            userinput = input("Enter the suburb that you wish to know median house prices in: ").strip().title()
            result = suburb_df[suburb_df['suburb'] == userinput][['suburb', 'median_price','km_from_cbd']].drop_duplicates(subset='suburb')
            #result = df[df[['suburb'] == userinput][['suburb', 'median_price']]]
            if result.empty:
                print("Suburb Not found, Try again.")
            else:
                print(result)

        elif choice == 3:
            main_menu()
            

