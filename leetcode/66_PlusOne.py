class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        place = 0
        # ith = 0
        # sum = 0
        newList = []
        for i in range (int(len(digits)), 0, -1):    
            # ith = i * pow(10, place)
            if (i == int(len(digits))):
                newList.append(digits[i-1] + 1)
            else:

                newList.append(digits[i-1])
            place += 1
            # sum += ith
        newList.reverse()
        return newList
        print(newList)

sol = Solution()
# sol.plusOne([1,2,3])
# sol.plusOne([4,3,2,1])
sol.plusOne([9])