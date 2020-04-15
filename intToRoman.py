class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic1 = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        dic2 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""
        index = 0
        while index < 13:
            while num >= dic2[index]:
                num -= dic2[index]
                result += dic1[index]
            index += 1
        return result

if __name__ == '__main__':
    a = Solution()
    print (a.intToRoman(3848))
