class Solution:
    def Unique(self, s, p):
        for i in s:
            if i in p:
                s = s.replace(i, "")
                p = p.replace(i, "")
        if len(s) == len(p):
            return True
        else:
            return False


def main():
    s = "dears"
    p = "dear"
    ret = Solution().Unique(s, p)
    print(ret)


if __name__ == '__main__':
    main()
