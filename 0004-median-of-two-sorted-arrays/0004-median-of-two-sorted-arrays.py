class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        merged_array=[0]*(m+n)
        def solve(i:int,j:int,k:int):
            if i<0 and j<0:
                return
            if i<0:
                merged_array[k]=nums2[j]
                solve(i,j-1,k-1)
            elif j<0:
                merged_array[k]=nums1[i]
                solve(i-1,j,k-1)
            elif nums1[i]>nums2[j]:
                merged_array[k]=nums1[i]
                solve(i-1,j,k-1)
            else:
                merged_array[k]=nums2[j]
                solve(i,j-1,k-1)
        solve(m-1,n-1,m+n-1)
        total=m+n
        mid=(m+n)//2
        if total%2==1:
            return float(merged_array[mid])
        else:
            return (float(merged_array[mid])+float(merged_array[mid-1]))/2


            
