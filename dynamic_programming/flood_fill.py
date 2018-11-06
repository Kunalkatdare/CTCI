class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(sr, sc):
            if image[sr][sc] == color:
                image[sr][sc] = newColor
                if sr >= 1: dfs(sr-1, sc)
                if sr+1 < R: dfs(sr+1, sc)
                if sc >= 1: dfs(sr, sc-1)
                if sc+1 < C: dfs(sr, sc+1)

        dfs(sr, sc)
        return image

def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            image = stringToInt2dArray(line)
            line = lines.next()
            sr = stringToInt(line)
            line = lines.next()
            sc = stringToInt(line)
            line = lines.next()
            newColor = stringToInt(line)
            
            ret = Solution().floodFill(image, sr, sc, newColor)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
