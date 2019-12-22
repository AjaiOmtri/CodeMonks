from itertools import permutations
# value = 30
# coins = [25, 10, 5]

# value = 11
# coins = [9, 6, 5, 1]

value = 121
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

num_of_coins_final = 999  # Counter to check how many total coins are there
accum_final = {}  # Final chosen total denominations


def coin_it(v, c):
    """
    Take the each sorted list of coins and use "divmod" function to
    fetch the number of coins required to make up the value
    """
    accum = {i: None for i in coins}
    for item in c:
        rem = divmod(v, item)
        accum[item] = rem[0]
        v = rem[1]
    return accum


for per_coins in list(permutations(coins)):
    """
    Take the coin list and generate the total number of ways you can sort the coin list.
    Call the function coin_it for each sort and find how many total coins it is generating
    Chose the denomination that has less number of coins
    """
    accum_temp = coin_it(value, per_coins)
    num_of_coins = sum(list(accum_temp.values()))
    if num_of_coins < num_of_coins_final:
        num_of_coins_final = num_of_coins
        accum_final = accum_temp

print(num_of_coins_final)
print(accum_final)

