# -*- coding: utf-8 -*-
import pandas as pd


def get_prediction(country_code, event_category):
    df = pd.read_csv("data/ebengtraining_small.csv",
                           usecols=['currency', 'id', 'country', 'category_id',
                                    'price_ticket_amount', 'purchased_at', 'quantity_sold'])
    # filter by category and country
    subset_df_filter_one = df.query('country == "US" & category_id == "101.0"')

    # filter by date
    # convert_date = df['purchased_at'] = pd.to_datetime(df['purchased_at'])
    # date_before = '26-01-2019'
    # mask = (df['purchased_at'] > date_before)
    # filter_by_date = df.loc[mask]

    subset_df_filter_date = subset_df_filter_one.loc[(subset_df_filter_one['purchased_at'] < '26-01-2019')]

    # calculate ticket price per unit
    price_ticket_per_unit = subset_df_filter_date['price_ticket_amount']/subset_df_filter_date['quantity_sold']
    mean_ticket = price_ticket_per_unit.mean()
    std_ticket = price_ticket_per_unit.std()

    print ("The mean is: {}, and standard is: {}.".format(mean_ticket, std_ticket))


if __name__ == "__main__":
    # country_code_input = raw_input("Country: ")
    # event_category_input = raw_input("Category:( example : 101.0): ")
    get_prediction('US', 'Sports')
