class Solution:
    def Unique(self, s):
        return len(set(s)) == len(s)


def main():
    s = "asdfghjkl;qwertyuiop1234567890l"
    ret = Solution().Unique(s)
    print(ret)


if __name__ == '__main__':
    main()
