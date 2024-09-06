# Question: monte carlo simulation of a portfolio value after e.g 3 hours
initial_portfolio_value: int = 100
up: float = 1.03    # u = 1.03
down: float = 1 / 1.03  # down = 1 / up
first_event_effect: float = up  # t = 1
second_event_effect: float = down   # t = 2
third_event_effect: float = up  # t = 3

# Q: What is the value of the initial portfolio value after three time periods
portfolio_value_at_time_one = initial_portfolio_value * first_event_effect
portfolio_value_at_time_two = portfolio_value_at_time_one * second_event_effect
# portfolio_value_at_time_three = ?