class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array=[]
        for num in nums1:
            merge_array.append(num)
        for num in nums2:
            merge_array.append(num)
        merge_array.sort()
        n=len(merge_array)
        if n%2==0:
            mid=n//2
            return (merge_array[mid-1]+merge_array[mid])/2
        else:
            mid=n//2
            return merge_array[mid]

        

        