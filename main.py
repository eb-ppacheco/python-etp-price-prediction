# -*- coding: utf-8 -*-
import pandas as pd


def get_prediction(country_code, event_category):
    df = pd.read_csv("data/ebengtraining_small.csv",
                           usecols=['currency', 'id', 'country', 'category_id',
                                    'price_ticket_amount', 'purchased_at', 'quantity_sold'])
    # filter by category and country
    # TO DO -create and  validate an user input
    subset_df_filter_one = df.query('country == "US" & category_id == "101.0"')

    # filter by date
    # TO DO - create a variable to calculate timezone.now - 30 days
    subset_df_filter_date = subset_df_filter_one.loc[(subset_df_filter_one['purchased_at'] < '26-01-2019')]

    # calculate ticket price per unit
    price_ticket_per_unit = subset_df_filter_date['price_ticket_amount']/subset_df_filter_date['quantity_sold']
    # TO DO - validate if currency it's the same, it means that you can't divide USD/BRL
    mean_ticket = price_ticket_per_unit.mean()
    std_ticket = price_ticket_per_unit.std()

    print ("The mean is: {}, and standard is: {}.".format(mean_ticket, std_ticket))


if __name__ == "__main__":
    # country_code_input = raw_input("Country: ")
    # event_category_input = raw_input("Category:( example : 101.0): ")
    get_prediction('US', 'Sports')
