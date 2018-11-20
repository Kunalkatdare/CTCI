class Solution:
    def StringCompression(self, s):
        count = 1
        answer = []
        prev = s[0]
        for curr in s[1:]:
            if prev == curr:
                count += 1
            else:
                answer.append(prev+str(count))
                prev = curr
                count = 1
        answer.append(prev+str(count))
        answer = "".join(answer)
        if len(answer) > len(s):
            return s
        else:
            return answer

        return answer


def main():
    s = "aaaaaakkkksddssdsddwwww"
    result = Solution().StringCompression(s)
    print(result)


if __name__ == '__main__':
    main()
