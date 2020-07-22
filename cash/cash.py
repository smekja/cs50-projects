import cs50, math
amount = -1
coins = 0

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

while amount < 0:
    amount = cs50.get_float("Change owed: ")

cents = round(amount * 100)

if cents > 24:
    coins = round_down(cents / 25)
    cents = cents % 25
if cents > 9:
    coins = coins + round_down(cents / 10)
    cents = cents % 10
if cents > 4:
    coins = coins + round_down(cents / 5)
    cents = cents % 5
if cents > 0:
    coins = coins + cents

print(round(coins))

