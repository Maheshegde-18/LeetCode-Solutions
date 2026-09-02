class Solution(object):
    def uniformArray(self, nums1):
        nums2=[]
        for i in range(len(nums1)):
            nums2.append(i)
        for i in range(len(nums2)):
            if i%2==0:
                return True
            return False
        