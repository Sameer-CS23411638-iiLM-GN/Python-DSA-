class Solution:
    def floor(self,root,x=10):
        ans = -1
        temp = root
        while temp is not None:
            if temp.data <= x:
                ans = temp.data
                temp = temp.right
            else:
                temp = temp.left
        return ans