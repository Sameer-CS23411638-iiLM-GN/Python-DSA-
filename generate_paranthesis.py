# n = 2
# ans = ["(())","()()"]
# def solve(ind,total,Brackets,result):
#     if ind>=len(Brackets):
#         if total == 0:
#             result.append("".join(Brackets))
#         return
#     if total>len(Brackets)//2:
#         return
#     elif total<0:
#         return
#     brackets[ind] = "("
#     sum = total+1
#     solve(ind+1,sum)
#     brackets[ind]=")"
#     sum = total-1
#     solve = (ind+1,sum)
#     brackets = [""]*(n*2)

n = 2

def solve(open_count, close_count, brackets, result):
    if len(brackets) == 2 * n:
        result.append("".join(brackets))
        return
    
    # place '('
    if open_count < n:
        brackets.append("(")
        solve(open_count + 1, close_count, brackets, result)
        brackets.pop()
    
    # place ')'
    if close_count < open_count:
        brackets.append(")")
        solve(open_count, close_count + 1, brackets, result)
        brackets.pop()

result = []
solve(0, 0, [], result)
print(result)