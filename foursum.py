class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        quad=[]
        sums=0
        nums = sorted(nums)
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while(left<right):
                    sums=nums[left]+nums[right]+nums[i]+nums[j]
                    if(sums==target):
                        temp = [nums[i],nums[j],nums[left],nums[right]]
                        if temp not in quad:
                            quad.append(temp)
                        left=left+1
                        right=right-1
                    elif(sums<target):
                        left=left+1
                    else:
                        right=right-1
        return quad



        