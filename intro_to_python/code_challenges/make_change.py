
def num_coins(cents):
    """
    Function makes changes given a number of cents.
    Coins : quarter (25), dime (10), nickel (5), pennies (1)
    :param cents:
    :return: the number of different coins in a given amount of cents
    """
    # Example: if num_coins(31) the function should return 3 (1 quarter, 1 nickel and 1 penni)
    if cents < 1:
        return 0

    coins = [25, 10, 5, 1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += cents / coin
        cents = cents % coin
        if cents == 0:
            break

    return num_of_coins

def min_coins(cents):
    # no nickels example
    # return the solution with the least number of pennies and possible coins
    coins = [25,10, 5,1]
    cents_temp = cents
    min_num_of_penni = {}
    for i in range(len(coins)):
        num_of_coins = {}
        cents = cents_temp
        if cents < coins[i]:
            continue
        for coin in coins[i:]:
            if cents < 1:
                num_of_coins[coin] = num_of_coins.get(coin, 0)
            num_of_coins[coin] = int(cents / coin)
            cents = cents % coin
        min_num_of_penni[coins[i]] = sum(num_of_coins.values())

    print(min_num_of_penni)
    return(min(min_num_of_penni.values()))


print(min_coins(70))
print(min_coins(2))
print(min_coins(25))