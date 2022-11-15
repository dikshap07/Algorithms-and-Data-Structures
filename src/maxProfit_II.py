def maxProfit_II(prices):

    maxProfit = 0

    for i in range(len(prices)-1):

        if prices[i] < prices[i+1]:

            maxProfit+= (prices[i+1] - prices[i])  #can simply add because we can buy/sell on the same day
    



    return maxProfit