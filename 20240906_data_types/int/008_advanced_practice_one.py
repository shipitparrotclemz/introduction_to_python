"""
Let's say you sell a call option at 100 USD

Now, your portfolio will decrease in value if the price of the stock goes up

To hedge your investment, you can buy X of stocks to protect your position
when the stock goes up

The X number of stocks follow this formula

stocks_to_buy_at_time_zero =
    (price_of_option_if_it_goes_up_in_value_at_time_1 - price_of_option_if_it_goes_down_in_value_at_time_1) /
    (price_of_stock_if_it_goes_up_at_time_1 - price_of_stock_if_it_goes_down_at_time_1)

Set
price_of_option_if_it_goes_up_in_value_at_time_1 = 200
price_of_option_if_it_goes_down_in_value_at_time_1 = 50
price_of_stock_if_it_goes_up_at_time_1 = 100
price_of_stock_if_it_goes_down_at_time_1 = 90

Print out stocks_to_buy_at_time_zero

You have to define 5 variables
"""

price_option_up_time_one: int = 200
