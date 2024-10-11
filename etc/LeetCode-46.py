class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.generatePermutations(nums, [], result)
        return result
    
    def generatePermutations(self, elements, current, result):
        if len(elements) == 0 :
            result.append(current)
            return
        
        for i in range(len(elements)):
            new = elements[:i] + elements[i+1:]
            self.generatePermutations(new, current + [elements[i]], result)
            
            
solution = Solution()
elements = [1, 2, 3, 4]
print(solution.permute(elements))