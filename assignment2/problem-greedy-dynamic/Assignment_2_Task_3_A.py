
#Given an array of coins $ c1 < c2 < . . . < c_n $, the objective is to determine the fewest coins needed to achieve a total of N.
def greedyNumCoins(coins, N):
    #Sort the coins
    coins.sort(reverse=True)
    NumberCoinsUsed = 0
    CoinsUsed = []
    #Go through each coin
    for coin in coins:
        #While you still can subtract the coin value
        while N >= coin:
            N -= coin
            CoinsUsed.append(coin)
            NumberCoinsUsed += 1
       #If the total is Zero, return the number of coins used
        if N == 0:
            return NumberCoinsUsed, N, CoinsUsed
    #Failed
    return -1, -1, []


def main():
    # Test case 1
    currency1 = [1, 5, 10, 20]
    N1 = 111
    NumberOfCoinsUsed, LeftOfTotal, CoinsUsed = greedyNumCoins(currency1, N1)
    print("N: ", N1,"\nNumber of coins used: ", NumberOfCoinsUsed, "\nCoinsUsed: ", CoinsUsed, "\nLeft of total: ", LeftOfTotal)

    #Test case 2
    currency2 = [1, 3, 22, 34]
    N2 = 123
    NumberOfCoinsUsed, LeftOfTotal, CoinsUsed = greedyNumCoins(currency2, N2)
    print("N: ", N2,"\nNumber of coins used: ", NumberOfCoinsUsed, "\nCoinsUsed: ", CoinsUsed, "\nLeft of total: ", LeftOfTotal)
    
    #Test case 3, where currency does not provice optimal output
    currency1 = [1, 5, 11]
    N1 = 15
    NumberOfCoinsUsed, LeftOfTotal, CoinsUsed = greedyNumCoins(currency1, N1)
    print("N: ", N1,"\nNumber of coins used: ", NumberOfCoinsUsed, "\nCoinsUsed: ", CoinsUsed, "\nLeft of total: ", LeftOfTotal)

main()