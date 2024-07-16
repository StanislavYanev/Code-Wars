# def count_change(money, coins):
#     change = [0] * (money + 1)
#     change[0] = 1
#     for coin in coins:
#         for i in range(coin, money + 1):
#             change[i] += change[i - coin]
#     return change[money]

def count_change(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    return count_change(money - coins[-1], coins) + count_change(money, coins[:-1])


# print(count_change(4, [1,2])) # => 3
print(count_change(10, [5, 2, 3]))  # => 4
# print(count_change(11, [5,7])) # => 0
