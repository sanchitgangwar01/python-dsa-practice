prices = [7,2,1,5,6,4,8]

# n=len(prices)
# def best_time_to_buy_and_sell_stock(prices):
#     max_profit=0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if prices[j]>prices[i]:
#                 p=prices[j]-prices[i]
#                 max_profit=max(max_profit,p)
#     return max_profit

# print(best_time_to_buy_and_sell_stock(prices))

#best optimal solution
def max_profit(prices):
    max_profit=0
    min_price=float("inf")
    n=len(prices)
    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit

print(max_profit(prices))