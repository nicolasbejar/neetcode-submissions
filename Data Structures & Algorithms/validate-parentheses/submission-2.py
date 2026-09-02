class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oppposite = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in s:
            if i in oppposite.keys():
                stack.append(i)
                continue
            
            elif stack and oppposite[stack[-1]] ==  i:
                stack.pop()
            else:
                return False
            
        if stack == []:
            return True
        else:
            return False