def maxProfit(prices):

    minPrice = float('inf')
    maxProfit = 0

    for i in range(len(prices)):

        if prices[i] < minPrice:

            minPrice = prices[i]

        elif prices[i] - minPrice > maxProfit:

            maxProfit = prices[i] - minPrice

    return maxProfit


print(maxProfit([7,1,2,3,4,5,6,3]))