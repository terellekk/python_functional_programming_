def dis(price, discount):
    discounted_price = price - (price * discount / 100)
    dp_round = round(discounted_price, 2)
    return dp_round
dis(1500, 50)