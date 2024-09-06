"""
You have a portfolio of 200 dollars

You invest in a stock of 10 dollars per share, and you buy 10 units

For the remaining amount of money, you invest it in the risk free interest rate market

which gives you an interest rate of 5% after 1 year

Lets say the stock increased in value of 6% after 1 year

Calculate the portfolio value after 1 year

Concepts:
- float * int = float
- int / int  = float
- int * int = int
- your * occurs first before +, if you want to + first, put brackets
"""

stock_value: int = 10 * 10  # 100
stock_value_after_one_year: float = 1.06 * stock_value  # new: float * int = float
interest_rate_value: int = 100
interest_rate_value_after_one_year: float = 1.05 * interest_rate_value
portfolio_after_one_year: float = stock_value_after_one_year + interest_rate_value_after_one_year
print(portfolio_after_one_year)     # 211.0