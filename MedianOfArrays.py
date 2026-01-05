def findMedianSortedArrays(a, b):
    nums=sorted(a+b)
    n=len(nums)
    return (nums[n//2] if n%2 else (nums[n//2-1]+nums[n//2])/2)
