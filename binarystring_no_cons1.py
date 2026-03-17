# class Solution:
#     def Solve(self,index,flag,numbers,result):
#         if index >= len(numbers):
#             result.append("".join(numbers))
#             return
#         numbers[index]="0"
#         self.solve(index+1,True,numbers,result)
#         if flag == True:
#             numbers[index] = "1"
#             self.Solve(index+1,False,numbers,result)
#             numbers[index] = "0"
# def generateBinarystrings(self,n):
#     numbers= [0]*n 
#     result = []
#     self.solve(0,True,numbers,result)
#     return result

class Solution:
    def solve(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        
        # place 0
        numbers[index] = "0"
        self.solve(index + 1, True, numbers, result)
        
        # place 1 only if previous was not 1
        if flag:
            numbers[index] = "1"
            self.solve(index + 1, False, numbers, result)

    def generateBinarystrings(self, n):
        numbers = [""] * n
        result = []
        self.solve(0, True, numbers, result)
        return result
obj = Solution()
print(obj.generateBinarystrings(3))