import pandas as pd


def get_prediction(country_code_input, event_category_input):
    df = pd.read_csv("data/ebengtraining_small.csv",
                     usecols=['currency', 'id', 'country', 'category_id',
                              'price_ticket_amount', 'purchased_at', 'quantity_sold'])
    cci = country_code_input
    eci = event_category_input

    # filter by country
    subset_filter_country = (df.loc[df['country'] == cci])

    # filter by category
    subset_filter_category = (subset_filter_country.loc[df['category_id'] == eci])

    # filter by date
    # TO DO - create a variable to calculate timezone.now - 30 days
    subset_df_filter_date = subset_filter_category.loc[(subset_filter_category['purchased_at'] < '26-01-2019')]

    # calculate ticket price per unit
    price_ticket_per_unit = subset_df_filter_date['price_ticket_amount']/subset_df_filter_date['quantity_sold']

    # TO DO - validate if currency it's the same, it means that you can't divide USD/BRL
    # validate if has a result
    if price_ticket_per_unit.empty:
        print ("Unfortunaly we can't provide data, the dataframe it's empty.")
    else:
        mean_ticket = price_ticket_per_unit.mean()
        std_ticket = price_ticket_per_unit.std()
        maximum = price_ticket_per_unit.max()
        print ("The mean is: {}, and standard is: {} and maximum is:{}.".format(mean_ticket, std_ticket, maximum))


if __name__ == "__main__":
    country_code_input = str(raw_input("Country::( example : US) "))
    event_category_input = float(raw_input("Category:( example : 101.0, 113.0): "))
    get_prediction(country_code_input, event_category_input)
