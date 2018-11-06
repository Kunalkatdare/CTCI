class Solution(object):
    def generateParenthesis(self, n):
        def generate(current, opening_params_available, unclosed_opening_params):
            #if we have used all "(" and need to close the paranthesis
            if opening_params_available == 0:
                return (current+')'*unclosed_opening_params)
            #if we have used all ")" and need to open the paranthesis
            elif unclosed_opening_params == 0:
                return generate(current+'(', opening_params_available-1, unclosed_opening_params+1)
            #if we do have unclosed "(", we need to add either ")" or "("
            return generate(current+'(', opening_params_available-1, unclosed_opening_params+1) + generate(current+')', opening_params_available, unclosed_opening_params-1)
        
        if n==0:
            return []
        return generate('', n, 0)

def stringToInt(input):
    return int(input)

def stringArrayToString(input):
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
            n = stringToInt(line)
            
            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
