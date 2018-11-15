class Solution:
    def Result(self, s, length):
        s = s.rstrip()
        for i in s:
            s = s.replace(" ", "%20")
        return s


def main():
    s = "Mr John Doe  "
    length = len(s)
    res = Solution().Result(s, length)
    print(res)


if __name__ == '__main__':
    main()
