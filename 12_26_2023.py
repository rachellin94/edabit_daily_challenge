def exchange_money(budget, exchange_rate):
    budget = float(budget)
    exchange_rate = float(exchange_rate)
    exchange_value = float(budget / exchange_rate)
    return exchange_value

    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

def get_change(budget, exchanging_value):
    budget = float(budget)
    exchanging_value = float(exchanging_value)  
    exchange_money_left = float(budget - exchanging_value)
    return exchange_money_left
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """



def get_value_of_bills(denomination, number_of_bills):
    denomination = int(denomination)
    number_of_bills = int(number_of_bills)
    value_of_the_bills = denomination * number_of_bills
    return value_of_the_bills
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """



def get_number_of_bills(amount, denomination):
    amount = float(amount)
    denomination = int(denomination)
    number_of_bills = int(amount / denomination)
    return number_of_bills 
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """


def get_leftover_of_bills(amount, denomination):
    amount = float(amount)
    denomination = int(denomination)
    leftover_of_bills_value = float(amount % denomination)
    return leftover_of_bills_value
    
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """


def exchangeable_value(budget, exchange_rate, spread, denomination):
    budget = float(budget)
    exchange_rate = float(exchange_rate)
    spread = int(spread)
    denomination = int(denomination)
    exchange_rate_spread_new = float(spread / 100) * exchange_rate
    exchange_rate_new = exchange_rate_spread_new + exchange_rate
    currency_exchanged = float(budget / exchange_rate_new)
    result = (currency_exchanged // denomination) * denomination
    return result 
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass

