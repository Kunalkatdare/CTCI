class Solution:
    def isSubstring(self, s, p):
        if len(s) != len(p):
            return False
        temp = s+s
        if p in temp:
            return True
        else:
            return False


def main():
    s1 = "waterbottle"
    s2 = "erbottlewat"
    ret = Solution().isSubstring(s1, s2)
    print(ret)


if __name__ == '__main__':
    main()
