class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        total=(m+n)
        mid=(total)//2
        prev=cur=0
        i,j=0,0
        for _ in range(mid+1):
            prev=cur
            if i==m:
                cur=nums2[j]
                j=j+1
            elif j==n:
                cur=nums1[i] 
                i+=1
            elif nums1[i]<nums2[j]:
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        if total%2==1:
            return cur
        else:
            return (prev+cur)/2