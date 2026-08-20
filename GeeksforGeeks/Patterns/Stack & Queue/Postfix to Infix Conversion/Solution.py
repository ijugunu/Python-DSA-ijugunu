class Solution:
    def postToInfix(self, postfix):
        
        self.stack=[]
        for ch in postfix:
            if ("A"<=ch<="Z") or ("a"<=ch<="z") or ("0"<=ch<="9"):
                self.stack.append(ch)
            else:
                item=""
                top1=self.stack.pop()
                top2=self.stack.pop()
                item="("+top2+ch+top1+")"
                self.stack.append(item)
        return self.stack.pop()    