def findDuplicates(nums):
    res=[]
    for n in nums:
        if nums[abs(n)-1]<0:
            res.append(abs(n))
        else:
            nums[abs(n)-1]*=-1
    return res
