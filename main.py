import pandas as pd
import csv



def main():
    # Read all data files
    csv1 = pd.DataFrame(pd.read_csv('data/daily_sales_data_0.csv'))
    csv2 = pd.DataFrame(pd.read_csv('data/daily_sales_data_1.csv'))
    csv3 = pd.DataFrame(pd.read_csv('data/daily_sales_data_2.csv'))

    # Get all in one Data Frame
    concatenaded_rows = pd.concat([csv1,csv2,csv3],axis=0)
    concatenaded_rows['price'] = concatenaded_rows['price'].str.replace('$','',regex=False)
    concatenaded_rows['price'] = pd.to_numeric(concatenaded_rows['price'], errors='coerce')

    #Get data only for the Pink morsel product
    condition = concatenaded_rows['product'] != 'pink morsel'
    to_drop = concatenaded_rows[condition].index
    new_df = concatenaded_rows.drop(to_drop)

    #create the sales column by sum the price and quantity
    new_df['sales'] = new_df['price'] * new_df['quantity']

    #final data with columns: Sales, Date and Region
    final_df = new_df[['sales','date', 'region']]

    # Save the final dataset in a csv file
    final_df.to_csv('cleaned_data.csv', index=False)
    


if __name__ == "__main__":
    main()
