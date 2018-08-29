def max_profit(prices):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.
    :param prices:
    :return:
    """
    if not prices:
        return 0

    max_profit, max_price = (0,0)
    for price in prices[::-1]:
        max_price = max(max_price, price)
        max_profit = max(max_profit, max_price - price)

    return max_profit