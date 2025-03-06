
import sys

#Given an array of coins $ c1 < c2 < . . . < c_n $, the objective is to determine the fewest coins needed to achieve a total of N.
#Always finding the optimal solution
def greedyNumCoinsOptimal(coins, N):
    arr = [sys.maxsize] * (N + 1)
    arr[0] = 0  # Base case

    for coin in coins:
        for i in range(coin, N + 1):
            arr[i] = min(arr[i], arr[i - coin] + 1)

    if arr[N] == sys.maxsize: 
        return -1
    
    return arr[N]


def main():
    # Test case 1 producing optimal solution, where a greeedy algorihtm would fail
    currency1 = [1, 5, 11]
    N1 = 15
    NumberOfCoinsUsed = greedyNumCoinsOptimal(currency1, N1)
    print("N: ", N1, "\nCurrency", currency1, "\nNumber of coins used: ", NumberOfCoinsUsed)


main()