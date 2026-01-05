def maximalRectangle(matrix):
    if not matrix: return 0
    heights=[0]*len(matrix[0])
    res=0
    for row in matrix:
        for i,v in enumerate(row):
            heights[i]=heights[i]+1 if v=="1" else 0
        res=max(res,largestRectangleArea(heights))
    return res
