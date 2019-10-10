#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Compute the maximum value of the sum of integers according  #
#                        to the rule on one line.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

import sys

if __name__ == "__main__":
    print("Enter the numbers [ctrl+d to exit]: ")
    x = [list(map(int, l.split(","))) for l in sys.stdin]
    dp = x[0]

    for i in range(1, (len(x)+1) // 2):
        _dp = [0] * (i+1)
        for j in range(i):
            _dp[j] = max(_dp[j], dp[j] + x[i][j])
            _dp[j+1] = max(_dp[j+1], dp[j] + x[i][j+1])
        dp = _dp

    for i in range((len(x) + 1) // 2, len(x)):
        _db = [0] * (len(dp)-1)
        for j in range(len(_dp)):
            _dp[j] = max(dp[j], dp[j+1], x[i][j])
        dp = _dp

    print(f"Maximum value of the sum of integers passing "
          f"according to the rule on one line: {dp[0]}")
