class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        l = []
        total = len(s)
        for x in s:
            if len(l) == 0:
                l.append(x)
                maxlen = 1
            else:
                if x not in l:
                    l.append(x)
                    if len(l) > maxlen:
                        maxlen = len(l)
                    print("new:%s, %d" , l, maxlen)
                else:
                    if len(l) > maxlen:
                        maxlen = len(l)
                    l = l[l.index(x)+1:]
                    l.append(x)

        return maxlen

if __name__ == '__main__':
    a = Solution()
    #print(a.lengthOfLongestSubstring("nfpdmpi"))
    print(a.lengthOfLongestSubstring("dvdf"))
    #s = ['d','v','f']
    #print (s[s.index('d')+1:])
