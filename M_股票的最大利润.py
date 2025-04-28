"""

字节-支付一面:

股票的最大利润:

假设把某股票的价格按照时间先后顺序存储在数组中，
请问买卖该股票一次可能获得的最大利润是多少？

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""


'''动态规划'''


def maxProfit(prices):

    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # 更新最低价格
        min_price = min(min_price, price)
        # 更新最大利润
        max_profit = max(max_profit, price - min_price)

    return max_profit


'''迭代遍历'''


def maxProfit2(prices):

    if not prices:
        return 0

    max_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit



if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
    print(maxProfit2(prices))
