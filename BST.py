def isValidBST(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if not lo < root.val < hi: return False
    return isValidBST(root.left, lo, root.val) and isValidBST(root.right, root.val, hi)
