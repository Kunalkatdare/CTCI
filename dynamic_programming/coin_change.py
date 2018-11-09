class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j>=i:
                    dp[j] += dp[j-i]
        return dp[amount]

def stringToInt(input):
    return int(input)

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            amount = stringToInt(line)
            line = lines.next()
            coins = stringToIntegerList(line)
            
            ret = Solution().change(amount, coins)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
