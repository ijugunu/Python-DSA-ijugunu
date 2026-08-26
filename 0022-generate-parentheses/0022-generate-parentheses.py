class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(index,total,brackets,result):   
            if index>=len(brackets):
                if total==0:
                    result.append("".join(brackets.copy()))
                return
            if total>len(brackets)//2:
                return
            if total<0:
                return 
            
            brackets[index]="("
            sum=total+1
            backtrack(index+1,sum,brackets,result)
            brackets[index]=")"
            sum=total-1
            backtrack(index+1,sum,brackets,result)
        
        brackets=[""]*(2*n)
        backtrack(0,0,brackets,result)
        return result