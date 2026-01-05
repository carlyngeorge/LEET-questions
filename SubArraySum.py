def subarraySum(nums, k):
    d={0:1}
    s=0
    res=0
    for n in nums:
        s+=n
        res+=d.get(s-k,0)
        d[s]=d.get(s,0)+1
    return res
